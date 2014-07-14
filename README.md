NI Courseware
==========
This repo maintains files under the Drupal /sites/all directory. Hopefully, this will make sharing easier without the need to have the entire Drupal source code in the repo.

Requirements
---
* PHP 5.3.3
* Drupal 7.22
* Python Fabric
* drush

Install
---
* ```cd``` into the directory you want to install Drupal
* Download drupal using drush: ```drush dl drupal-7.22```
* Move into the ```sites``` directory ```cd <drupal>/sites```
* Remove the __all__ directory ```rm all``` or rename it ```mv all old_all```
* Clone repo into __sites__ as  __all__ ```git@github.com:smithandrobot/courseware.git all```
* Checkout and switch to the dev branch ```git checkout -t origin/dev```

Drupal
---
* Drush is installed

* Modules  
Custom modules go in modules/custom  
Contributed modules go into modules/contrib

* Theme  
Custom themes go in themes/custom  
Contributed themes go into themes/contrib, in case of sub-themeing