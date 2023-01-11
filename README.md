# Algorithm-Project

## Scenario
Nowadays, people have become more oblivious to the nutritional values that various food may offer, as the nutritional values may differ from one another based on their structure and quantity. Such conundrum has brought upon a lot of recurring problems to an individual who wishes to stay fit in their physical form as well as abstaining certain bad food consumption behaviors which may lead to underlying health problems. If we narrow down the scope to the fitness or bodybuilding world, we would be able to acknowledge that the main nutrients that a bodybuilder has to consider are mainly protein, calories and carbohydrates (carbs). Protein is essential in helping body cells to repair and build new ones, whereas calories are the amount of energy released to conduct an activity when our body breaks down the food. Carbs on the other hand are sugar molecules that provides energy for body cells, but overdosing the carbs intake may ruin the whole workout process as the excess sugar molecules will then be converted into fats. Ideally, when planning a diet an athlete or fitness trainer has to optimize their diet by consuming the maximum intake of protein for muscle building, the maximum amount of calories in order to have the energy for fitness training as well as the minimum amount of carbs to prevent from getting excessive fats.

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
### 0-1 Knapsack Problem
A user wanted to obtain the maximum of protein or calories in his/her diet, with minimum amount of carbs intake. We denote all relevant variables as follows:

W = Capacity,the maximum number of carbs intake  
wt = Weight,the nutritional values of carbs  
val = Profit, the nutritional values of protein or calories  
n = Number list of carbs being considered  
K[][] = Temporary 2D Array, 0-1 Knapsack Table  
res = Maximum profit, the maximum amount of protein or calories gained  

To obtain any values in any given point of the 2D Array (0-1 Knapsack Table). We have:

K[i][w] = max( K[i-1][w] ,  K[i-1 , w - wt[i] ] + val[i] )

Where i = 0,1,2 … n
      w = 0,1,2 … W

To obtain the maximum profit, we have:

res = K[n][W]


### Fractional Knapsack Problem
In a case of a Fractional knapsack problem, the food may be broken down into smaller portions and servings instead of taking it as a whole unit. We then denote all relevant variables as follows:

W = Capacity,the maximum number of carbs intake  
wt = Weight,the nutritional values of carbs  
val = Profit, the nutritional values of protein or calories  
n = Number list of carbs being considered  
res = Maximum profit, the maximum amount of protein or calories gained  

In a case where the food is broken down into smaller intake portions for maximum profit optimization, we have:
![image](https://user-images.githubusercontent.com/96568739/211497634-54da7bd6-2e7a-4c6f-8cbb-4ed75866f0fa.png)  
To obtain the maximum profit, we have:  
![image](https://user-images.githubusercontent.com/96568739/211497882-d3bf005c-d7ab-46a9-b176-c95360a0e672.png)

 



           
