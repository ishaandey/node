# Lab 6: Google's AI-Powered App

### Goal

We will be exploring Google's debut app that can diagnose skin conditions based on photos of the consumer's skin. It's fairly new and could potentially help a bunch of people that could be walking around with harmful skin conditions. This example of a real world use of a ML classification model highlights the ways certain companies are utilizing machine learning.

Article: [Google debuts AI-powered app to help consumers identify common skin conditions](https://www.fiercehealthcare.com/tech/google-previews-ai-dermatology-tool-to-help-consumers-identify-skin-conditions)

### Your Task

After reading the article and by **using your knowledge of how machine learning models are trained**, tackle the following questions under a group discussion:

1. If you were at Google, what kind of data would you need to train the model?
2. How would you validate the model? Be specific - how big would the project be, who would you need to recruit, etc.?
3. What might be some problems of a dataset with the following pictures (besides not enough data)?
    ![training image](images/training-img.png)
4. How could we prevent the problem(s) of a dataset similar to the one above? Hint: It's not *just* about the training data

## Discussion Responses

### W 5:30 PM Lab
1. If you were at Google, what kind of data would you need to train the model?
- Supervised, classification model
- Put labels on there first, group them
- Identify the groups, need the training data and testing data
- Lots of pictures of things that are moles/skin conditions and those that aren't
- Getting data pertaining to individuals --> skin color, race, gender/sex
2. How would you validate the model? Be specific - how big would the project be, who would you need to recruit, etc.?
- If testing, release it beta testers --> validate through them as they meet with their doctor/dermatologist
- Doing biopsies, different scans they can do --> having that data/technology
3. What might be some problems of a dataset with the following pictures (besides not enough data)?
- skin tone is only white, not diverse
4. How could we prevent the problem(s) of a dataset similar to the one above? Hint: It’s not just about the training data.
- avoiding mistakes in the model: more information awareness, consult a doctor, don't take results to heart
- obviously, get more data, but easier said than done. loading more data on diverse skin colors and tones

### W 7:00 PM Lab

1. If you were at Google, what kind of data would you need to train the model?
- Lots of images: both ones with the disease and healthy skin pictures, as well as pictures of skin & nails.
- Doctors feedback & classification 
- Medical data, symptoms 
2. How would you validate the model? Be specific - how big would the project be, who would you need to recruit, etc.?
- Validate the model by comparing the model’s results with data from the doctors and a chunk of the data used specifically for testing.
- Running the model with all the images and asking many professionals to see their diagnoses.
- The project seems very big. The researchers need a large amount of images, data about diseases, and professionals to validate the model. If we were doing this, we would need to recruit ML experts, Dermatologists, and people willing to share their personal data/images. 
3. What might be some problems of a dataset with the following pictures (besides not enough data)?
- Clarity (middle: blurry)
- 1st and 3rd are the same (remove duplicates)
- Lack of variety in skin color
- Removing non-skin photos
- What part of the body is it?
4. How could we prevent the problem(s) of a dataset similar to the one above? Hint: It’s not just about the training data.
- Inclusivity: diverse range of skin tones
- Better instructions on how to take the photo; examples for those sending photos

### Th 4:00 PM Lab

1. If you were at Google, what kind of data would you need to train the model?
- Database of images of people's skin conditions
- Search information: key words within the search to classify each disease
- Different variations of each possible skin trait --> healthy vs. not healthy data
- Database with all of the conditions for skin and what they are
- Ethical concerns: specified search --> don't want to get rid of good information but also have enough to make proper results
- Wide range of ages and skin tones so it'll be able 
2. How would you validate the model? Be specific - how big would the project be, who would you need to recruit, etc.?
- Test cases with doctors --> Human validation
- Take pictures of already diagnosed skin conditions and run it through the model, look at result
3. What might be some problems of a dataset with the following pictures (besides not enough data)?
- Varying image quality, some are blurry, some not
- All the pictures are of people with similar skin tones, need more variety
4. How could we prevent the problem(s) of a dataset similar to the one above? Hint: It’s not just about the training data.
- More variations of the data --> skin tone, different image qualities of the same photo
- Add in images with freckles and other marks that are completely harmless
- Filter out by image quality
