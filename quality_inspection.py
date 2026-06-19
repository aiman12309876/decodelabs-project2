import cv2
import numpy as np
import random

def create_test_image(defect=False):
    image = np.ones((300, 300, 3), dtype=np.uint8) * 200
    cv2.circle(image, (150, 150), 80, (100, 100, 100), -1)
    cv2.circle(image, (150, 150), 50, (150, 150, 150), -1)

    if defect:
        cv2.circle(image, (120, 130), 15, (0, 0, 0), -1)
        cv2.line(image, (170, 170), (190, 190), (0, 0, 0), 3)

    return image

def inspect_part(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 120, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    defects = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 50 and area < 300:
            x, y, w, h = cv2.boundingRect(contour)
            defects.append((x, y, w, h))

    return defects

def display_result(image, defects):
    result = image.copy()

    if defects:
        status = "FAIL"
        color = (0, 0, 255)
        for x, y, w, h in defects:
            cv2.rectangle(result, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(result, "DEFECT", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    else:
        status = "PASS"
        color = (0, 255, 0)

    cv2.putText(result, f"STATUS: {status}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("Quality Inspection", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    print("\n" + "=" * 60)
    print("   AUTOMATED QUALITY INSPECTION")
    print("=" * 60)

    print("\n[1] Creating test images...")

    good_part = create_test_image(defect=False)
    print("  Good part created")

    bad_part = create_test_image(defect=True)
    print("  Bad part created")

    print("\n[2] Inspecting Good Part...")
    defects = inspect_part(good_part)
    if defects:
        print(f"  Defects found: {len(defects)}")
    else:
        print("  No defects found - PASS")
    display_result(good_part, defects)

    print("\n[3] Inspecting Bad Part...")
    defects = inspect_part(bad_part)
    if defects:
        print(f"  Defects found: {len(defects)}")
        for d in defects:
            print(f"    - Defect at position: ({d[0]}, {d[1]})")
    else:
        print("  No defects found")
    display_result(bad_part, defects)

    print("\n" + "=" * 60)
    print("   INSPECTION COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main()