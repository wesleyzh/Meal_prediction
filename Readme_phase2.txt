Files:
logistic_regression.py :
 - require yummly.json in the same working directory
 - process the json data by pandas
 - train the logistic regression model based on yummly.json
 - report the performance of the created model
 - save the file in yummly_lg.pkl, so next time we do not need re-train the model

random_forest.py:
 - require yummly.json in the same working directory
 - process the json data by pandas
 - train the random forest model based on yummly.json
 - report the performance of the created model
 - save the file in yummly_rf.pkl, so next time we do not need re-train the model

project2_phase2.py:
 - ask for your choice of method: 1 for logistic regression, or 2 for random forest
 - load the selected model, i.e., yummly_lg.pkl or yummly_rf.pkl
 - ask for ingredients (e.g., baking powder,eggs,all-purpose flour,raisins,milk,white sugar) 
 - run the model and predict the cuisine (e.g., southern_us)
 - Function search_dishes(ingredients, N, df) print the top N closet meals with the ingredients

Steps for project 2 phase two:
1. open command line to the working directory
2. run: python logistic_regression.py (this can be skipped since I have uploaded the pkl file)
3. run: python random_forest.py (this can be skipped since I have uploaded the pkl file)
4. run: python project2_phase2.py
   4.1 Program asks the user to input all the ingredients that they are interested in.
   4.2 Program uses the model to predict the type of cuisine and tell the user.
   4.3 Program finds the top N closest foods (you can define N). Return the IDs of those dishes to the user.

Example:
C:\Users\WeiliZhang\Desktop\Project2>python logistic_regression.py
The logistic regression model is training...
The training process is completed and the total time is 72 seconds
Report of created logistic regression model:
             precision    recall  f1-score   support

  brazilian       0.90      0.72      0.80       467
    british       0.77      0.63      0.69       804
cajun_creole       0.85      0.79      0.82      1546
    chinese       0.85      0.91      0.88      2673
   filipino       0.87      0.77      0.82       755
     french       0.72      0.74      0.73      2646
      greek       0.88      0.81      0.84      1175
     indian       0.90      0.94      0.92      3003
      irish       0.82      0.64      0.72       667
    italian       0.86      0.93      0.89      7838
   jamaican       0.91      0.82      0.86       526
   japanese       0.90      0.78      0.84      1423
     korean       0.90      0.87      0.88       830
    mexican       0.93      0.95      0.94      6438
   moroccan       0.91      0.86      0.89       821
    russian       0.81      0.66      0.73       489
southern_us       0.79      0.86      0.82      4320
    spanish       0.76      0.62      0.68       989
       thai       0.85      0.85      0.85      1539
 vietnamese       0.83      0.67      0.74       825

avg / total       0.86      0.86      0.85     39774

The logistic regression model is saved in 'yumly_lg.pkl'

C:\Users\WeiliZhang\Desktop\Project2>python random_forest.py
The random forest model is training...
The training process is completed and the total time is 166 seconds
Report of created random forest model:
             precision    recall  f1-score   support

  brazilian       1.00      1.00      1.00       467
    british       1.00      1.00      1.00       804
cajun_creole       1.00      1.00      1.00      1546
    chinese       1.00      1.00      1.00      2673
   filipino       1.00      1.00      1.00       755
     french       1.00      1.00      1.00      2646
      greek       1.00      1.00      1.00      1175
     indian       1.00      1.00      1.00      3003
      irish       1.00      1.00      1.00       667
    italian       1.00      1.00      1.00      7838
   jamaican       1.00      1.00      1.00       526
   japanese       1.00      1.00      1.00      1423
     korean       1.00      1.00      1.00       830
    mexican       1.00      1.00      1.00      6438
   moroccan       1.00      1.00      1.00       821
    russian       1.00      1.00      1.00       489
southern_us       1.00      1.00      1.00      4320
    spanish       1.00      1.00      1.00       989
       thai       1.00      1.00      1.00      1539
 vietnamese       1.00      1.00      1.00       825

avg / total       1.00      1.00      1.00     39774

The randomforest model is saved in 'yumly_rf.pkl'

C:\Users\WeiliZhang\Desktop\Project2>python project2_phase2.py
Please enter the classfier 1 (logistic regression) or 2 (random forest): 1
Please enter ingredients seperated by comma: baking powder,eggs,all-purpose flou
r,raisins,milk,white sugar
Your input ingredients are:
baking powder,eggs,all-purpose flour,raisins,milk,white sugar
Predicted cuisine by logistic regression is: british

Do you want print meals with the ingredients? (Y/N)Y
How many meals you want to see?3

Meal 1:26100, eggs , all-purpose flour

The system does not find enough meals matches your input.
Do you want to see related meals? (Y/N) Y

Meal 2:18911, ground cinnamon , honey , raisins , toasted walnuts , orange , dar
k rum , salt , dried fig , eggs , unsalted butter , vanilla extract , white suga
r , milk , baking powder , all-purpose flour

Meal 3:23824, eggs , milk , butter , all-purpose flour , ground cloves , baking
powder , raisins , chopped pecans , pecan halves , ground nutmeg , lemon , hot w
ater , ground cinnamon , orange , flaked coconut , cocktail cherries , white sug
ar

C:\Users\WeiliZhang\Desktop\Project2>python project2_phase2.py
Please enter the classfier 1 (logistic regression) or 2 (random forest): 2
Please enter ingredients seperated by comma: baking powder,eggs,all-purpose flou
r,raisins,milk,white sugar
Your input ingredients are:
baking powder,eggs,all-purpose flour,raisins,milk,white sugar
Predicted cuisine by logistic regression is: southern_us

Do you want print meals with the ingredients? (Y/N)Y
How many meals you want to see?3

Meal 1:26100, eggs , all-purpose flour

The system does not find enough meals matches your input.
Do you want to see related meals? (Y/N) Y

Meal 2:18911, ground cinnamon , honey , raisins , toasted walnuts , orange , dar
k rum , salt , dried fig , eggs , unsalted butter , vanilla extract , white suga
r , milk , baking powder , all-purpose flour

Meal 3:23824, eggs , milk , butter , all-purpose flour , ground cloves , baking
powder , raisins , chopped pecans , pecan halves , ground nutmeg , lemon , hot w
ater , ground cinnamon , orange , flaked coconut , cocktail cherries , white sug
ar
