from simple_image_download import simple_image_download as simp

# from simp library call simple_image_download function
response = simp.simple_image_download

# the keywords that will be used to find pics, and each key work will create a different file 
keywords = ["Motor Helmet","Bike Helmet"]

# for loop on the keywords
# (kw, 300) means 300 sample of each keyword
for kw in keywords:
    response().download(kw, 60) 
