import cv2
import mediapipe as mp
import math
import time

# ============================================================
# SETTINGS
# ============================================================

EYE_CLOSED_THRESHOLD = 0.23

# How long eyes must remain closed
DROWSY_TIME = 2.0
SLEEP_TIME = 4.0

# Yawning
YAWN_THRESHOLD = 0.50
YAWN_TIME = 1.0

# Alarm / suspension
ALARM_THRESHOLD = 70       # Highest individual score
ALARM_TIME = 2.0

SUSPEND_THRESHOLD = 60     # Class average score
SUSPEND_TIME = 5.0

# ============================================================
# MEDIAPIPE
# ============================================================

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=10,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# ============================================================
# CAMERA
# ============================================================

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("ERROR: Camera could not be opened")
    exit()

print("Camera started")
print("Press Q to quit")

# ============================================================
# TIMERS
# ============================================================

eye_closed_start = {}
yawn_start = {}

alarm_start = None
suspend_start = None

# ============================================================
# FUNCTIONS
# ============================================================

def distance(p1, p2):
    return math.sqrt(
        (p1.x - p2.x) ** 2 +
        (p1.y - p2.y) ** 2
    )


def eye_aspect_ratio(landmarks, eye_points):

    p1 = landmarks[eye_points[0]]
    p2 = landmarks[eye_points[1]]
    p3 = landmarks[eye_points[2]]
    p4 = landmarks[eye_points[3]]
    p5 = landmarks[eye_points[4]]
    p6 = landmarks[eye_points[5]]

    vertical1 = distance(p2, p6)
    vertical2 = distance(p3, p5)
    horizontal = distance(p1, p4)

    if horizontal == 0:
        return 0

    return (vertical1 + vertical2) / (2.0 * horizontal)


def mouth_ratio(landmarks):

    top = landmarks[13]
    bottom = landmarks[14]
    left = landmarks[78]
    right = landmarks[308]

    vertical = distance(top, bottom)
    horizontal = distance(left, right)

    if horizontal == 0:
        return 0

    return vertical / horizontal


# ============================================================
# EYE LANDMARKS
# ============================================================

LEFT_EYE = [
    33, 160, 158,
    133, 153, 144
]

RIGHT_EYE = [
    362, 385, 387,
    263, 373, 380
]

# ============================================================
# MAIN LOOP
# ============================================================

while True:

    ret, frame = cap.read()

    if not ret:
        print("ERROR: Could not read frame")
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    current_time = time.time()

    student_scores = []

    sleeping_count = 0
    drowsy_count = 0
    yawning_count = 0
    normal_count = 0

    # ========================================================
    # FACE PROCESSING
    # ========================================================

    if results.multi_face_landmarks:

        for student_id, face in enumerate(
            results.multi_face_landmarks
        ):

            landmarks = face.landmark

            # ------------------------------------------------
            # EAR
            # ------------------------------------------------

            left_ear = eye_aspect_ratio(
                landmarks,
                LEFT_EYE
            )

            right_ear = eye_aspect_ratio(
                landmarks,
                RIGHT_EYE
            )

            ear = (left_ear + right_ear) / 2

            # ------------------------------------------------
            # MOUTH
            # ------------------------------------------------

            mouth = mouth_ratio(landmarks)

            # ------------------------------------------------
            # EYE CLOSED TIMER
            # ------------------------------------------------

            if ear < EYE_CLOSED_THRESHOLD:

                if student_id not in eye_closed_start:
                    eye_closed_start[student_id] = current_time

                closed_duration = (
                    current_time -
                    eye_closed_start[student_id]
                )

            else:

                eye_closed_start.pop(
                    student_id,
                    None
                )

                closed_duration = 0

            # ------------------------------------------------
            # YAWN TIMER
            # ------------------------------------------------

            if mouth > YAWN_THRESHOLD:

                if student_id not in yawn_start:
                    yawn_start[student_id] = current_time

                yawn_duration = (
                    current_time -
                    yawn_start[student_id]
                )

            else:

                yawn_start.pop(
                    student_id,
                    None
                )

                yawn_duration = 0

            # =================================================
            # STATE CLASSIFICATION
            # =================================================

            if closed_duration >= SLEEP_TIME:

                state = "SLEEPING"
                probability = 100

                sleeping_count += 1

            elif closed_duration >= DROWSY_TIME:

                state = "DROWSY"
                probability = 70

                drowsy_count += 1

            elif yawn_duration >= YAWN_TIME:

                state = "YAWNING"
                probability = 40

                yawning_count += 1

            else:

                state = "NORMAL"
                probability = 0

                normal_count += 1

            # Store student's probability
            student_scores.append(probability)

            # =================================================
            # DRAW FACE MESH
            # =================================================

            mp_drawing.draw_landmarks(
                frame,
                face,
                mp_face_mesh.FACEMESH_TESSELATION,
                mp_drawing.DrawingSpec(
                    color=(0, 0, 255),
                    thickness=1,
                    circle_radius=1
                ),
                mp_drawing.DrawingSpec(
                    color=(255, 255, 255),
                    thickness=1
                )
            )

            # =================================================
            # STUDENT INFORMATION
            # =================================================

            # Position near top-left of face
            x = int(landmarks[10].x * frame.shape[1])
            y = int(landmarks[10].y * frame.shape[0])

            cv2.putText(
                frame,
                f"{state} {probability}%",
                (x - 60, y - 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 255),
                2
            )

            # Show EAR for debugging
            cv2.putText(
                frame,
                f"EAR:{ear:.2f}",
                (x - 60, y + 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.45,
                (255, 255, 255),
                1
            )

    # ========================================================
    # CLASS PROBABILITY / SCORE
    # ========================================================

    student_count = len(student_scores)

    if student_count > 0:

        class_probability = (
            sum(student_scores) /
            student_count
        )

        highest_probability = max(
            student_scores
        )

    else:

        class_probability = 0
        highest_probability = 0

    # ========================================================
    # ALARM TIMER
    # ========================================================

    if highest_probability >= ALARM_THRESHOLD:

        if alarm_start is None:
            alarm_start = current_time

        alarm_duration = (
            current_time - alarm_start
        )

    else:

        alarm_start = None
        alarm_duration = 0

    alarm_active = (
        alarm_duration >= ALARM_TIME
    )

    # ========================================================
    # CLASS SUSPENSION TIMER
    # ========================================================

    if class_probability >= SUSPEND_THRESHOLD:

        if suspend_start is None:
            suspend_start = current_time

        suspend_duration = (
            current_time - suspend_start
        )

    else:

        suspend_start = None
        suspend_duration = 0

    class_suspended = (
        suspend_duration >= SUSPEND_TIME
    )

    # ========================================================
    # DISPLAY INFORMATION
    # ========================================================

    cv2.putText(
        frame,
        f"Students: {student_count}",
        (30, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Class Drowsiness: {class_probability:.0f}%",
        (30, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Highest Student: {highest_probability:.0f}%",
        (30, 110),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 200, 255),
        2
    )

    cv2.putText(
        frame,
        f"Sleeping: {sleeping_count}",
        (30, 145),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (0, 0, 255),
        2
    )

    cv2.putText(
        frame,
        f"Drowsy: {drowsy_count}",
        (30, 175),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (0, 165, 255),
        2
    )

    cv2.putText(
        frame,
        f"Yawning: {yawning_count}",
        (30, 205),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255, 255, 0),
        2
    )

    # ========================================================
    # STATUS
    # ========================================================

    if class_suspended:

        status = "CLASS SUSPENDED"

        cv2.putText(
            frame,
            status,
            (30, 255),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            (0, 0, 255),
            3
        )

    elif alarm_active:

        status = "DROWSINESS ALARM"

        cv2.putText(
            frame,
            status,
            (30, 255),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            (0, 0, 255),
            3
        )

    else:

        status = "CLASS NORMAL"

        cv2.putText(
            frame,
            status,
            (30, 255),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            (0, 255, 0),
            3
        )

    # ========================================================
    # SHOW WINDOW
    # ========================================================

    cv2.imshow(
        "Classroom Drowsiness Detection",
        frame
    )

    # Q = quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# ============================================================
# CLEANUP
# ============================================================

cap.release()
cv2.destroyAllWindows()
face_mesh.close()

print("Program closed.")