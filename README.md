# 5800-Final-Project
Route Optimization in Travel Plan


**Author:**

Yixiao Zhu, Xin Sun, Haoning Wang.



**Description:**

This is a the final project of CS5800 Algorithms course.

Our project  fills a void in the mapping application market by offering users a personalized and optimized visiting itinerary to parks in Vancouver. Users only need to input their preferences, and the program will print out the results. Maybe the results are not perfect, but they can address the problem quite a lot.

Our solution is carefully crafted, taking into account the user's current location, their daily park visit capability, and their preferred park facilities. 

Our approach involved leveraging official data from government public databases of Vancouver city, meticulously gathering and organizing this data to compile a comprehensive list of Vancouver's parks, complete with their names, geographical coordinates, and available facilities. An innovation in our project is the 'Utility Coefficient', a bespoke parameter that quantifies the value of each park based on the quantity of facilities and their alignment with user preferences. This coefficient plays a crucial role in determining the weight of different routes in our model. In devising the optimal routing strategy, we enhanced the traditional Minimum Spanning Tree (MST) algorithm to align more closely with practical user requirements, thereby ensuring that our users are provided with the most efficient and enjoyable park visiting experiences.




**Usage:**
To use the program, run _main_program.py_, and type in the number of parks:

![image](https://github.com/EthanLawyer/5800-Final-Project/assets/133042033/1188f12a-6218-43ec-b0b3-965328ed143d)


then choose from the 34 facilities which you wish to enjoy at the parks to visit:

![image](https://github.com/EthanLawyer/5800-Final-Project/assets/133042033/dac92a33-d6f9-43e3-bf49-1dd1c56620c0)

and the program will suggest an optimized route of visit:

![image](https://github.com/EthanLawyer/5800-Final-Project/assets/133042033/6d7a5ece-d1c2-4b4f-a3d6-2f05d2f4a93a)

