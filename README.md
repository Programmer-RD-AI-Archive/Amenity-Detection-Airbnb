# Amenity Detection

- Table of Content
  Project Idea
  Why am I doing this Project
  Article Summary
  Target of this Project (Goals)
  What I want to learn
  Todo List
  Resources
  Blog / Tracking

---

# Project Idea

- The Idea is that Airbnb A Few Years ago create an Object Detection Model to Detect Amenities or like objects in an image so they can give better search results to their customer.
- So what I am trying to do is since it has been a few years later I am going to try and get a better model and overall better than Airbnb Model

---

# Why am I doing this Project?

- I want to do a long project so I am going to do data analytics more because I don't do any of that so I want to learn about data analytics and other stuff that section is below
- And Just for Fun, I haven't done something like this ever so I am excited.

---

# Article Summary

![1_zcbhlQfmeWNmOlFyaPGPfg.png](Amenity%20Detection%20b761326f55b343119108923b622b6195/1_zcbhlQfmeWNmOlFyaPGPfg.png)

- The above is an example image that they tell that their models predicted.
  - So for the above Image, I want my model to get much better performance than it 🙂
- What Airbnb Tried
  - TensorFlow Detection Model Zoo
    [models/research/object_detection at master · tensorflow/models](https://github.com/tensorflow/models/tree/master/research/object_detection)
  - Detectron Model Zoo
    [Detectron/MODEL_ZOO.md at main · facebookresearch/Detectron](https://github.com/facebookresearch/Detectron/blob/main/MODEL_ZOO.md)
  - Small Note - They didn't use Detectron2 Which is the newer and the better version of detectron
  - Small Note - None of The Models Satisfied their Requirements
- Data Used
  ![https://miro.medium.com/max/1842/1*_MrE7H_D2YF_4T9FrMa62Q.png](https://miro.medium.com/max/1842/1*_MrE7H_D2YF_4T9FrMa62Q.png)
  - Classes or Labels that they used (They mean Airbnb)
  - They used Open Image V4
    [Open Images V6](https://storage.googleapis.com/openimages/web/index.html)
    - Structure of Open Images
      [Flare Dendrogram](https://storage.googleapis.com/openimages/2018_04/bbox_labels_600_hierarchy_visualizer/circle.html)
  - They used 40 classes
  - They had a total of 100K images !!
    - And 50K was from Open Images or They annotated the data
  - Average of 1.2K of Images Per Class or Label
  - They used google data labeling service
    1. It supports up to 100 Labels for Labelling
    2. A Clean and Good UI
  ![1_jXaptuvICwSOTmsz1f5RFQ.png](Amenity%20Detection%20b761326f55b343119108923b622b6195/1_jXaptuvICwSOTmsz1f5RFQ.png)
  - How Airbnb Created their DataSet
  - 43K Internal 32K Public
- Model Training
  - faster_rcnn_inception_resnet_v2 _and ssd_mobilenet_v2 was the fastest but accuracy_
  - The Metric They Care about is mAP or mean Average Precision \*\*
    - _ssd_mobilenet_v2 got over 54% map_
  - They did some feature extraction
  - The target of mAP was at least 50%
  - Because all of the custom models was not working they had to use Google AutoML
    - In which they cant download the data
    - They got 68% mAP in 7.5K test images
    ![1_FmMhkEo44LSq5A4CEdl6KA.png](Amenity%20Detection%20b761326f55b343119108923b622b6195/1_FmMhkEo44LSq5A4CEdl6KA.png)
    ![1_zfGRutWEIYwo9_1UFCA5PA.png](Amenity%20Detection%20b761326f55b343119108923b622b6195/1_zfGRutWEIYwo9_1UFCA5PA.png)

---

# The target of this Project (Goals)

- Not Spend Money
  - Run all of the models and everything locally
    - GPU - RTX 3060
    - RAM - 32GB
    - CPU = Ryzen 5 3600
    - Motherboard - MSI B450
- Get over 50% mAP at least or get more performance than 68% mAP which is what Airbnb Got in their Google Auto-ml
- Host the App
- Create an API
- Cost-Effective and Better Performance than Airbnb

---

# What I want to learn

- Streamlit
- Detectron2
- Ray Tune
- Debugging
- Metrics
- More In-depth
- PyTorch Object Detection Maybe
- Data Analytics
  - Seaborn
  - Matplotlib
- preprocessing Methods
  - Normalization
  - Taxonomy
- File Structure
- Take more Time for the Data Analytics

---

# To-do List

- [ ] Download the Open Images dataset
- [ ] Data Analytics
  - First Create Sub-samples of the data
  - Then Train a model then check its performance
  - Then Try another Way
    - And I need to try all of the preprocessing methods I can find
- [ ] Creating the Final Data Set with the best methods I could find
- [ ] Parameter Tuning of the Models
- [ ] Repeat until the results are good
- [ ] Conclusion

---

[Resources](https://www.notion.so/082d410ccdd643edb28f410cb7df9685)
