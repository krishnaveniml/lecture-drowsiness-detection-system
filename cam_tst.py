import cv2

# ==========================================
# MULTI-STUDENT FACE DETECTION SYSTEM
# ==========================================

# Load Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Open laptop camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("ERROR: Camera could not be opened")
    exit()

print("Camera started...")
print("Press Q to quit")

while True:

    # Read camera frame
    ret, frame = cap.read()

    if not ret:
        print("ERROR: Could not read camera frame")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50)
    )

    # Draw rectangle around every detected face
    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )

    # Number of detected students
    student_count = len(faces)

    # Display student count
    cv2.putText(
        frame,
        f"Students detected: {student_count}",
        (40, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.5,
        (0, 255, 0),
        3
    )

    # Show camera window
    cv2.imshow(
        "Multi-Student Face Detection",
        frame
    )

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release camera
cap.release()
cv2.destroyAllWindows()

print("Program closed.")