# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required


# @login_required
# def home(request):
#  return render(request, "index.html", {})
 



# def authView(request):
#  if request.method == "POST":
#   form = UserCreationForm(request.POST or None)
#   if form.is_valid():
#    form.save()
#    return redirect("base:login")
#  else:
#   form = UserCreationForm()
#  return render(request, "registration/signup.html", {"form": form})



# def index(request):
#     return render(request, 'index.html')
  
  
  
  
  
  
  
  
  
  

# from django.shortcuts import render
# from django.core.files.storage import FileSystemStorage
# import tensorflow as tf
# from PIL import Image
# import numpy as np 

# # Function to load the pre-trained model
# def load_model():
#     # Assuming the model is saved as 'trained.h5' in your project directory
#     model_path = 'C:/Users/DELL/Desktop/NAVA/LoginSignup/loginsignup/models/model.h5'
#     model = tf.keras.models.load_model(model_path)
#     return model

# # Function to preprocess the uploaded image
# def preprocess_image(image_path):
#     # Load the image
#     img = Image.open(image_path)

#     # Resize the image to the model's expected input size
#     target_size = (64, 64)  # Replace with your model's input size
#     img = img.resize(target_size)

#     # Convert to a NumPy array and normalize pixel values
#     img_array = tf.keras.preprocessing.image.img_to_array(img) / 255.0

#     # Expand dimensions for the model's input format (batch size, height, width, channels)
#     img_array = np.expand_dims(img_array, axis=0)

#     return img_array

# # View function to handle image upload and prediction
# def predictImage(request):
#     if request.method == 'POST':
#         print(request)
#         print(request.POST.dict())
#         print("HELLLOOOOOOOOOOO")
#         print(request.FILES)
#         fileObj = request.FILES['filePath']
#         fs = FileSystemStorage()
#         filePathName = fs.save(fileObj.name, fileObj)
#         filePathName=fs.url(filePathName)
#         context = {'filePathName': filePathName}
#         print(filePathName)

#         # Load the pre-trained model (ensure it's loaded only once)
#         if not hasattr(predictImage, 'model'):
#             predictImage.model = load_model()

#         # Preprocess the uploaded image
#         img_array = preprocess_image(fs.path(filePathName))

#         # Make prediction using the model
#         predictions = predictImage.model.predict(img_array)

#         # Get the class with the highest probability
#         predicted_class_index = np.argmax(predictions[0])
#         # predicted_class_index=predicted_class_index-1
#         print(predicted_class_index)

#         # Load the class labels (assuming they're stored in a list named 'class_labels')
# #         class_labels = ['Corn leaf blight',
# #  'Tomato leaf',
# #  'Tomato leaf mosaic virus',
# #  'Potato leaf',
# #  'Squash Powdery mildew leaf',
# #  'Potato leaf late blight',
# #  'Soyabean leaf',
# #  'Peach leaf',
# #  'Tomato leaf late blight',
# #  'Apple leaf',
# #  'Tomato mold leaf',
# #  'Corn Gray leaf spot',
# #  'Tomato leaf yellow virus',
# #  'Strawberry leaf',
# #  'Cherry leaf',
# #  'Apple rust leaf',
# #  'Potato leaf early blight',
# #  'grape leaf black rot',
# #  'Apple Scab Leaf',
# #  'Tomato Septoria leaf spot',
# #  'Tomato leaf bacterial spot',
# #  'Blueberry leaf',
# #  'Bell_pepper leaf spot',
# #  'Corn rust leaf',
# #  'Bell_pepper leaf',
# #  'grape leaf',
# #  'Tomato two spotted spider mites leaf',
# #  'Tomato Early blight leaf',
# #  'Raspberry leaf']  # Replace with your actual labels
#         class_labels=['Pepper__bell___Bacterial_spot','Pepper__bell___healthy','Potato___Early_blight','Potato___Late_blight','Potato___healthy','Tomato_Bacterial_spot','Tomato_Early_blight','Tomato_Late_blight','Tomato_Leaf_Mold','Tomato_Septoria_leaf_spot','Tomato_Spider_mites_Two_spotted_spider_mite','Tomato__Target_Spot','Tomato__Tomato_YellowLeaf__Curl_Virus','Tomato__Tomato_mosaic_virus','Tomato_healthy']

#         # Extract the predicted disease label
#         predicted_disease = class_labels[predicted_class_index]

       
#         # , 'predicted_disease': predicted_disease
#         print(predicted_disease)
#         return render(request, 'index.html', context)

#     else:
#         return render(request, 'index.html')



from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import tensorflow as tf
from PIL import Image
import numpy as np

@login_required
def home(request):
    return render(request, "index.html", {})

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("base:login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def index(request):
    return render(request, 'index.html')

# Function to load the pre-trained model
def load_model():
    model_path = 'C:/Users/DELL/Desktop/NAVA/LoginSignup/loginsignup/models/model.h5'
    model = tf.keras.models.load_model(model_path)
    return model

# Function to preprocess the uploaded image
def preprocess_image(image_path):
    img = Image.open(image_path)
    target_size = (64, 64)  # Replace with your model's input size
    img = img.resize(target_size)
    img_array = tf.keras.preprocessing.image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# View function to handle image upload and prediction
def predictImage(request):
    if request.method == 'POST':
        fileObj = request.FILES['filePath']
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
        filename = fs.save(fileObj.name, fileObj)
        file_path = fs.path(filename)

        # Ensure the file path is within the MEDIA_ROOT
        if not file_path.startswith(settings.MEDIA_ROOT):
            return HttpResponseBadRequest("Invalid file path")

        context = {'filePathName': settings.MEDIA_URL + filename}

        # Load the pre-trained model (ensure it's loaded only once)
        if not hasattr(predictImage, 'model'):
            predictImage.model = load_model()

        # Preprocess the uploaded image
        img_array = preprocess_image(file_path)

        # Make prediction using the model
        predictions = predictImage.model.predict(img_array)

        # Get the class with the highest probability
        predicted_class_index = np.argmax(predictions[0])
        print(predicted_class_index)

        # Load the class labels (assuming they're stored in a list named 'class_labels')
        class_labels = ['Pepper__bell___Bacterial_spot','Pepper__bell___healthy','Potato___Early_blight','Potato___Late_blight','Potato___healthy','Tomato_Bacterial_spot','Tomato_Early_blight','Tomato_Late_blight','Tomato_Leaf_Mold','Tomato_Septoria_leaf_spot','Tomato_Spider_mites_Two_spotted_spider_mite','Tomato__Target_Spot','Tomato__Tomato_YellowLeaf__Curl_Virus','Tomato__Tomato_mosaic_virus','Tomato_healthy']

        # Extract the predicted disease label
        predicted_disease = class_labels[predicted_class_index]
        print(predicted_disease)
        context['predicted_disease'] = predicted_disease
        context = {'filePathName': settings.MEDIA_URL + filename,"predicted":predicted_disease}

        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
