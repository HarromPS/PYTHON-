# Image Resizer

# opencv helps in image, video processing, object, face, handriting identification
import cv2

# Read a image: cv2.imread(PATH, FLAG)
# _UNCHANGED = -1 , includes alpha channel while loading
# _COLOR = -1 , includes colorful image
# _GRAYSCALE = 0 , in grayscale
image = cv2.imread("A:\VS Codes\Programming\PYTHON\PROJECTS_PY\Image Resizer\demo.webp",cv2.IMREAD_UNCHANGED);

# show image: cv2.imshow("name of window", read image)
cv2.imshow("Indian man", image);

# scales
scaleBy = 50 # percent

# get new height & width
newHeight = int(image.shape[0] * scaleBy / 100);
newWidth = int(image.shape[1] * scaleBy / 100);

# tuple of height & width
tple = (newWidth, newHeight);

# get a new image using resizer
output = cv2.resize(image,tple);

# write a new image
cv2.imwrite("new.webp", output);

# wait for user to press key
cv2.waitKey(0);

