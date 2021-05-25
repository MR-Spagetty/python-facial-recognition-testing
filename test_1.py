import face_recognition
import PIL
from PIL import Image, ImageDraw
from face_recognition.api import face_encodings

faces = {}

test_image = face_recognition.load_image_file('biden.jpg')
two_people = face_recognition.load_image_file('two_people.jpg')

unkown_encodings = face_recognition.face_encodings(two_people)
face_locations = face_recognition.face_locations(two_people)

pil_image = Image.fromarray(two_people)

for encoding in unkown_encodings:
    known = face_recognition.compare_faces([face_recognition.face_encodings(test_image)[0]], encoding)
    if known[0]:

# print(face_recognition.face_encodings(test_image)[0])
# pil_image = Image.fromarray(two_people)
        squares = ImageDraw.Draw(pil_image, 'RGBA')
        location = face_locations[unkown_encodings.index(encoding)]
        squares.rectangle([(location[1], location[0]), (location[3], location[2])], outline='red', width=5)

pil_image.show()
