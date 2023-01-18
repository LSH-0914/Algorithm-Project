# Algorithm-Project

## Scenario
Nowadays, people have become more oblivious to the nutritional values that various food may offer, as the nutritional values may differ from one another based on their structure and quantity. Such conundrum has brought upon a lot of recurring problems to an individual who wishes to stay fit in their physical form as well as abstaining certain bad food consumption behaviors which may lead to underlying health problems. If we narrow down the scope to the fitness or bodybuilding world, we would be able to acknowledge that the main nutrients that a bodybuilder has to consider are mainly protein, calories and carbohydrates (carbs). Protein is essential in helping body cells to repair and build new ones, whereas calories are the amount of energy released to conduct an activity when our body breaks down the food. Carbs on the other hand are sugar molecules that provides energy for body cells, but overdosing the carbs intake may ruin the whole workout process as the excess sugar molecules will then be converted into fats. Ideally, when planning a diet an athlete or fitness trainer has to optimize their diet by consuming the maximum intake of protein for muscle building, the maximum amount of calories in order to have the energy for fitness training as well as the minimum amount of carbs to prevent from getting excessive fats.  
![image](https://user-images.githubusercontent.com/96568739/213096706-20733d70-beac-40d3-832c-bc1f10bcaea2.png)  

## Importance of Optimal Solution
### Improve effectiveness for athlete to decide their menus to consume suitable amount of protein to keep fit
Protein is the building block of your muscles.
Therefore, eating adequate amounts of protein helps athletes maintain the muscle mass and promotes muscle growth when they do strength training.
Numerous studies show that eating plenty of protein can help increase muscle mass and strength. If someone is physically active, lifting weights, or trying to gain muscle, they need to make sure getting enough protein. Keeping protein intake high can also help prevent muscle loss during weight loss. Thus, the optimal solution for this scenario is important and useful for athletes.

### Help people to maintain a healthy nutritional intake
By using our program, people can know how much the protein should they consume and the recommendation of food containing protein will also be portrayed. Sufficient protein consumption is good for our bones.  People who eat more protein tend to maintain bone mass better as they age and have a much lower risk of osteoporosis and fractures.
This is especially important for women, who are at high risk of osteoporosis after menopause. Eating plenty of protein and staying active is a good way to help prevent that from happening. It can also boost metabolism, increases fat burning and lower our blood pressure.

## Suitability of Sorting, DAC, DP, Greedy and Graph algorithms as a solution paradigm
![image](https://user-images.githubusercontent.com/96568739/211486399-a2d56e97-211c-4ce4-9952-60b9b5a9f2bc.png)

## Algorithm Specification
### Unbound 0-1 Knapsack Problem
A user wanted to obtain the maximum of protein or calories in his/her diet, with minimum amount of carbs intake. We denote all relevant variables as follows:

W = Capacity,the maximum number of carbs intake  
wt = Weight,the nutritional values of carbs  
val = Profit, the nutritional values of protein or calories  
n = Option of carbs    
K[][] = Temporary 2D Array, Unbound 0-1 Knapsack Table  
res = Maximum profit, the maximum amount of protein or calories gained  

To obtain any values in any given point of the 2D Array (Unbound 0-1 Knapsack Table). We have:

**K[i][w] = max( K[i-1][w] ,  K[i-1 , w - wt[i] ] + val[i] )**

Where i = 0,1,2 … n
      w = 0,1,2 … W

To obtain the maximum profit, we have:

**res = K[n][W]**


### Unbound Fractional Knapsack Problem
In a case of a Unbound Fractional Knapsack problem, the food may be broken down into smaller portions and servings instead of taking it as a whole unit. We then denote all relevant variables as follows:

W = Capacity,the maximum number of carbs intake  
wt = Weight,the nutritional values of carbs  
val = Profit, the nutritional values of protein or calories  
n = Option of carbs  
res = Maximum profit, the maximum amount of protein or calories gained  

In a case where the food is broken down into smaller intake portions for maximum profit optimization, we have:
![image](https://user-images.githubusercontent.com/96568739/211497634-54da7bd6-2e7a-4c6f-8cbb-4ed75866f0fa.png)  
To obtain the maximum profit, we have:  
![image](https://user-images.githubusercontent.com/96568739/211497882-d3bf005c-d7ab-46a9-b176-c95360a0e672.png)  
![Untitled Diagram](https://user-images.githubusercontent.com/96568739/212907794-7f8a60f9-36c0-473b-ac80-d93bed8a05e8.jpg)

## Idea Explanation of Algorithm Paradigm
Prior to jumping into the main part of the algorithm, our program will proceed to read the csv file for the nutrient dataset, which includes important elements to describe the data such as ‘food’, ‘protein/100g’, ‘carbs/100g’ and ‘calories’. The program allows user to input the types of food allergies the user may have towards a certain food before processing them with the algorithms. It will also prompt user to input whether they want a diet with optimum protein or optimum calories. With that, it will automatically discard the food rows which are similar to the allergic type input of the user and proceeds to append the remaining rows of datas to the food, carbs and protein/calories list respectively.  

![image](https://user-images.githubusercontent.com/96568739/211745968-ceb5ed4a-c9f9-4c6a-a5f1-0d360c877ddb.png)
![image](https://user-images.githubusercontent.com/96568739/211746075-4405f8e6-e8f3-420f-b14e-e07140fad7db.png)
**Figure 1: List Append & User Prompt**  

### Algorithm Design: Unbound 0-1 Knapsack Problem Using Dynamic Programming
The scenario of fitness trainer wanting to obtain the maximum amount of protein or calories with the minimum amount of carbs intake is equivalent to the Unbound 0-1 Knapsack problem which can be solved by dynamic programming. In a case of illustrating the knapsack problem with our scenario, the weight element in the knapsack problem will be our carbs, as it remains as a demerit factor or a constraint in obtaining the maximum profit, in which this case will be either protein or calories (depending on the diet planning selection of the individual).

Firstly, the program reads the input from the user about what food items he/her like to prioritize in his/her diet. A food list is also printed to prompt user to know what food is listed in the dataset. Besides that, the user also gets to input the intake quantity of the food item that he/she wishes to prioritise earlier. A while loop is provided to make sure that the user gets to input multiple food prioritizations. Such function in our program allows the user to be more flexible in planning his/her diet in the meantime of achieving the maximum protein/calories instead of solely following the food the system recommends, which in some case the user may only have access to certain food. (e.g. Some countries only have watercress stems as their vegetable crop production for a particular season, such feature will let the user to choose this food as their prioritization in the meantime of calculating the best diet for him/her) 

The program then proceeds to process the input data from the user by storing the food name, protein/calories and carbs of that particular food into the prioritize,prioritize1 and prioritize lists respectively. These preprocessed data in the arrays will be used for the Unbound 0-1 Knapsack algorithm which will be explained later on.  

![image](https://user-images.githubusercontent.com/96568739/211747936-1f29b287-c702-4096-9a0f-ad0d19b6a7d6.png)  
**Figure 2: Food Prioritization**  

Then, the program reads the input from the user about the number of carbs (in grams) he/she plan to consume, which then the input is stored as a capacity variable, $W$ in the knapsack problem. It then calls out the main function by passing through the parameters which are food as $name$ (Naming for each food item), carbs as $wt$ (weight of the knapsack problem) , protein as $val$ (value or profit for the knapsack problem; this variable could be storing protein or calories values depending on the user input as both serves the same goal for the program) and $n$ (an int variable of carbs list). With that, we are able to illustrate that the table of knapsack problem is constituted with ‘n’ rows and ‘W’ columns.  

![image](https://user-images.githubusercontent.com/96568739/211746778-4f318b5d-3d83-4231-bb72-45d0fa9e8be3.png)  
**Figure 3: Main function calling**  

The main code segments of the algorithm requires recurrence in order to get each result (K[n][W] variable) of the intersection of each data cells in the table which contains n rows and W columns for the Unbound 0-1 Knapsack table.  

![image](https://user-images.githubusercontent.com/96568739/211746924-d8232188-34b0-4d61-8a2f-10cb34f018b1.png)  
**Figure 4: Design Algorithm (Unbound 0-1 Knapsack Problem)**  

We start off by initializing the loop increment variables which is $w$ for $W$ and $i$ for $n$. The program will then loop through matrix to get their respective intersection cells’ value. In a case where $i$ or $w$ is equals to zero, the value stored in that intersection cell will be 0 as well (K[i][w] = 0). In a case where the capacity of the knapsack is able to store a weight (carb value in this case), then we take the maximum value of either the profit (val) of the weight, or the upper row value of the current cell (K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],K[i-1][w]). 

Last but not least we also run through another recurrence algorithm to print out the optimum protein obtained by the Unbound 0-1 Knapsack algorithm and the distribution of the carbohydrate and protein for those particular food that are suggested in diet planning.  

![image](https://user-images.githubusercontent.com/96568739/211747047-fd51a772-729d-4fdb-93ac-94de9eaf9e9f.png)   
**Figure 5: Design Algorithm (Unbound 0-1 Knapsack Problem)**  

![image](https://user-images.githubusercontent.com/96568739/211755225-81e90623-0536-4665-93f4-7858c4169e7c.png)  
**Figure 6: Output Unbound 0-1 Knapsack Problem**  

### Algorithm Design: Unbound Fractional Knapsack Problem
Even though we have temporarily given a resolution to the scenario with the Unbound 0-1 Knapsack problem, but the problem still retains as the obtained maximum profit from the Unbound 0-1 Knapsack problem wasn’t fully optimized. As to illustrate, the food are only taken as a whole unit by the individual without any exception of breaking it down to smaller portions with the design of Unbound 0-1 Knapsack problem.Thus, our team have came out with a more improvised algorithm to add on to the existing fundamentals of the Unbound 0-1 Knapsack problem, which is solving it with the Unbound Fractional Knapsack problem.

As a start to the program, it also receives input from the user about the maximum carbs they wanted to intake (capacity), then proceeds to store each variables with respective lists namely _n_ (food), _profit_ (protein) and _weight_ (carbs).

We then generate a list named _ratio_ to store the profit values per weight values for each food. Thus, we can conclude that the higher the _ratio_ value, the more profit it brings to the overall result. A list called index is also generated for n food items which is then sorted in a descending order according to their respective ratio values to be compared later.  
![image](https://user-images.githubusercontent.com/96568739/213096800-684437b0-80d0-4722-a0a5-ad206ec4ece1.png)  
![image](https://user-images.githubusercontent.com/96568739/211749868-04f5e468-fa16-4f3d-a120-68804b717da3.png)  
**Figure 7: Profit per weight values Sorting**  

Last but not least, we run through a for loop starting from the first index of the sorted index list (starting from the highest ratio). We compare it with the capacity(max carbs) provided by the user and if its in a case where its value is smaller than the capacity, we take the whole unit of the food and print out its description. In a case where it is bigger than the capacity, we will have to compute its fractional profit with some mathematical divisions and then add the remnants to the computed overall result.  

![image](https://user-images.githubusercontent.com/96568739/211810499-afa69fd7-386f-4ceb-affd-c10b20770a6d.png)  
**Figure 8: Design Algorithm (Fractional Knapsack)**  

![image](https://user-images.githubusercontent.com/96568739/211812180-d4aff262-bc81-455f-aead-d1fcdfb89388.png)  
**Figure 9: Output Unbound Fractional Knapsack Problem**  

As we can observe in the result illustrated from Figure 9, with the same amount of input in the Unbound 0-1 Knapsack problem, we get a higher profit constituted which is a total optimum protein of (188.2g) compared to what we have in Unbound 0-1 Knapsack (187g). With that, we conclude that this algorithm will give us more optimization in getting the maximum profit with the minimum amount of weight.  

## Algorithm's Correctness  
### Correctness Proof for Unbound 0-1 Knapsack Algorithm  
In order to proof that our formula in the Unbound 0-1 Knapsack Algorithm, which is obtaining any values in any given point of the 2D Array (Unbound 0-1 Knapsack Table), K[i][w] = max( K[i-1][w] ,  K[i-1 , w - wt[i] ] + val[i] ) is true, we will proceed to prove its correctness by using the induction method.  

First, the induction hypothesis is considered by:  

Pair (i,w) < (i',w') if i < i' or (i = i' and w < w').  

For example, at any given pair of values in the 2D Array, we get: 

(0,0) < (0,1) < (0,2) < (0,3) < … < (1,0) < (1,1) < …  

Induction Hypothesis : Thus, we can infer that the algorithm will be correct for all values of K[i][w] where (i,w) < (i',w'). All previous elements in the table are correct in this case of assumption.  

Base case: K[i][0] = K[0][w] = 0 for all values of i and w.  
 
The induction hypothesis will constitute K[i'-1][w'] ,  K[i'-1 , w'- wt[i'] to be true as they follow the constraint (i,w) < (i',w') for any set of values in the 2D Array. Thus, with that in a case where the item i' contains a weight (exist in the knapsack), we then consider its value, constituting us K[i'-1 , w'- wt[i'] + val[i']. On the other hand, in a case where the item i' does not contain a weight (absence in the knapsack), we do not consider its value, thus giving us K[i'-1][w']. By finding the maximum value from these two results in order to get the accurate value for that particular data set intersection in the 2D Array, we get max( K[i-1][w] ,  K[i-1 , w - wt[i] ] + val[i] ). Hence, the correctness for the Unbound 0-1 Knapsack algorithm’s formula is proven.  

### Correctness Proof for Unbound Fractional Knapsack Algorithm  
To show that the Unbound Fractional Knapsack algorithm provides optimization to the constitution of the maximum value obtained, we have to proof that it is indeed a greedy algorithm. With that, assuming that our Unbound Fractional Knapsack problem has a total capacity of W and packed with items such that $A= a_1,a_2,a_3,..a_n$. with respective values of $V =val_1,val_2,val_3,..val_n$ with weight quantities of $W = wt_1,wt_2,wt_3,..wt_n$. With that, picking a new choice from this filled knapsack would be $a_{n+1}$ with value-to-weight ratio of $val_{n+1}/wt_{n+1} > val_i/wt_i$ , assuming that i ranges from 1 to n. From here, we can see that a new optimal solution can be obtained with a replacement method such that:  

Let i = 1,2,3,…n and i ≠ j   
Where j is an index chosen such that $val_j/wt_j < val_i/wt_j$  

So if we replace $a_j$ with $a_{n+1}$, we get an objective function increment by $(val_{n+1}  - val_j / min(wt_{n+1},wt_j)$ .This will be the optimum possible increment as any other values other than $a_j$ replacement will constitute us a larger subtraction amount than  $val_j / min(wt_{n+1},wt_j)$. Thus, with that we proceeded to go through a recurrence replacement strategy by choosing  $j_k$ as the index of the remaining item with the lowest value-to-weight ratio for subtraction to get the highest value-to-weight ratio by replacing the whole knapsack until it is completely full of $a_i$. With that, we can prove that this Unbound Fractional Knapsack algorithm is a greedy algorithm.  

## Time Complexity  
![image](https://user-images.githubusercontent.com/96568739/211817256-b4af59f4-4eb3-4c4b-8cb7-fe406c5933e0.png)  

*where n is the number of carbs item and W is the maximum amount of carb intake input by user  
 










 



           
