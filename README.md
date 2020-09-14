# Project Overview

## Project Links

Link to completed project [here](https://emp4.netlify.app/#/).
Link to project frontend [here](https://github.com/emestiza/p4frontend).
Link to project backend [here](https://github.com/emestiza/p4backend).

## Project Schedule

|  Day | Deliverable | Status
|---|---| ---|
|Day 1| Project Description | Complete
|Day 1| Wireframes / Priority Matrix / Timeline `backend` and `frontend`| Complete
|Day 2| Working RestAPI | Incomplete
|Day 3| Core Application Structure (HTML, CSS, etc.) | Incomplete
|Day 4| Core Application Structure (Vue.js) | Incomplete
|Day 5| MVP & Bug Fixes | Incomplete
|Day 6| Final Touches and Present | Incomplete

## Project Description

The goal of this project is to build an information database full stack application for school and studying puroposes. The API in the backend is built using Python, Django, and PSQL. The API has three models and two associations. The user model is associated to the subject model and the subject model is associated to the topic model. There is Create, Read, Update, and Destroy (CRUD) functionality built throughout the application models. In the frontend JavaScript and Vue.js are used to connect and leverage the backend API. While HTML and CSS are used for styling and organization purposes. The fronend also has a responsive design for mobile, tablet, and desktops. 

## Wireframes

Below are links to wireframes that show the application blueprint for mobile, tablet, and desktop display sizes.

- [Mobile](https://res.cloudinary.com/dssciwyew/image/upload/v1599931278/Mobile%20P4.png)
- [Tablet](https://res.cloudinary.com/dssciwyew/image/upload/v1599931278/Tablet%20P4.png)
- [Desktop](https://res.cloudinary.com/dssciwyew/image/upload/v1599931278/Desktop%20P4.png)

Models

```
class Subject(models.Model):
    class Meta:
        verbose_name_plural = 'subjects'

    name = models.CharField(max_length = 100)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length = 100)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, related_name = 'topics', on_delete = models.CASCADE)
    description = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_public = models.BooleanField(default = False)

    def __str__(self):
        return self.name
```

## Time/Priority Matrix 

Here is a full list of features that have been [prioritized](https://res.cloudinary.com/dssciwyew/image/upload/v1599935146/Priority%20Matrix%20Backend%20P4.png) using a `Time and Priority` Matix. 

### MVP/PostMVP

The functionality will then be divided into two separate lists: MPV and PostMVP.  The contents in the MVP list are expect to be implemented and functioning upon project completion. 

#### MVP

- JWT Authentication
- User model
- Subject Model
- Topic Model
- Routes
- Migration
- Deploy and test on Heroku
- Test on Postman

#### PostMVP 

- Filter data functionality
- Abililty to share user public user links

## Functional Components

Based on the initial logic defined in the previous sections, the logic is broken down further into functional components.

#### MVP
| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| JWT Authentication | H | 2hrs | 2hrs | 2hrs|
| User model | H | 1hr | 1hr | 1hr|
| Subject Model | H | 1hr | 1hr | 1hr|
| Topic Model | H | 1hr| 1hr | 1hr |
| Routes | H | 1hr | 1hr | 1hr|
| Migration | H | 1hrs| 1hr | 1hr |
| Deploy & test on Heroku | H | 1hr | 1hr | 1hr|
| Test on Postman | M | 1hr | 1hr | 1hr|
| Reasearch & Development | M | 2hrs | 2hrs | 2hrs|
| Debugging | M | 2hrs | 2hrs | 2hrs|
| Total |  | 13hrs| 13hrs | 13hrs |

#### PostMVP
| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Filter data functionality| L | 2hrs | 0hrs | 0hrs|
| Total | H | 2hrs| 0hrs | 0hrs |

## Additional Libraries
 Use this section to list all supporting libraries and thier role in the project. 

## Code Snippet

Use this section to include a brief code snippet of functionality that you are proud of an a brief description  

```
function reverse(string) {
	// here is the code to reverse a string of text
}
```

## Issues and Resolutions
 Use this section to list of all major issues encountered and their resolution.

#### SAMPLE.....
**ERROR**: app.js:34 Uncaught SyntaxError: Unexpected identifier                                
**RESOLUTION**: Missing comma after first object in sources {} object
