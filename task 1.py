import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("D:\python cv\Yog1a.jpg")
# Getting the image's width and height.pi
img_width = img.shape[1]
img_height = img.shape[0]
# Creating a figure and a set of axes.
fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('off')
ax.imshow(img [...,::-1])
plt.show()
# Initializing the Pose and Drawing modules of MediaPipe.
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
with mp_pose.Pose(static_image_mode=True) as pose:
    """
    This function utilizes the MediaPipe library to detect and draw 'landmarks'
    (reference points) on an image. 'Landmarks' are points of interest
    that represent various body parts detected in the image.
    Args:
        static_image_mode: a boolean to inform if the image is static (True) or sequential (False).
    """
    # Make a copy of the original image.
    annotated_img = img.copy()
    # Processes the image.
    results = pose.process(img)
    # Set the circle radius for drawing the 'landmarks'.
    # The radius is scaled as a percentage of the image's height.
    circle_radius = int(.007 * img_height)
    # Specifies the drawing style for the 'landmarks'.
    point_spec = mp_drawing.DrawingSpec(color=(220, 100, 0), thickness=-1, circle_radius=circle_radius)
    # Specifies the drawing style for landmark connections.
    line_spec = mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2)
    # Draw the 'landmarks' on the image.
    mp_drawing.draw_landmarks(annotated_img,
                    landmark_list=results.pose_landmarks,
                    connections=mp_pose.POSE_CONNECTIONS,
                    landmark_drawing_spec=point_spec,
                    connection_drawing_spec=line_spec)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.axis('off')
    ax.imshow(annotated_img [...,::-1])
    plt.show()