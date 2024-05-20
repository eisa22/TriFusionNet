import YOLO

if __name__ == "__main__":
    # Control Panel
    # Choose camera idx: 0 for laptop webcam; idx:1 for external camera
    camera_idx = 0

    # Choose if webcam should be active (True) or image should be used (False)
    webcam = False

    # Image path
    image_path = 'Images/Table_with_objects.jpg' # Images/Sliding_Window_Results/subimage22.jpg

    detector = YOLO.ObjectDetection(camera_idx, webcam, image_path)
    detector()

