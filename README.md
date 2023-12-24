# 5800-Final-Project
## Route Optimization in Travel Plan

**Authors:** Yixiao Zhu, Xin Sun, Haoning Wang

### Project Description

This project is the culmination of our work in the CS5800 Algorithms course.

Our project fills a gap in the mapping application market by providing users with a personalized and optimized visiting itinerary for parks in Vancouver. Users only need to input their preferences, and the program will generate the results. While the results may not be perfect, they address the problem significantly.

Our solution is carefully crafted, taking into account the user's current location, their daily park visit capability, and their preferred park facilities.

We leveraged official data from government public databases of Vancouver city, meticulously gathering and organizing this data to compile a comprehensive list of Vancouver's parks, complete with their names, geographical coordinates, and available facilities. An innovation in our project is the 'Utility Coefficient,' a bespoke parameter that quantifies the value of each park based on the quantity of facilities and their alignment with user preferences. This coefficient plays a crucial role in determining the weight of different routes in our model. In devising the optimal routing strategy, we enhanced the traditional Minimum Spanning Tree (MST) algorithm to align more closely with practical user requirements, thereby ensuring that our users are provided with the most efficient and enjoyable park visiting experiences.

### Usage

To use the program, run _main_program.py_, and follow these steps:

1. Input the number of parks.

![Number of Parks](https://github.com/EthanLawyer/5800-Final-Project/assets/133042033/1188f12a-6218-43ec-b0b3-965328ed143d)

2. Choose from the 34 facilities you wish to enjoy at the parks to visit.

![Facilities Selection](https://github.com/EthanLawyer/5800-Final-Project/assets/133042033/dac92a33-d6f9-43e3-bf49-1dd1c56620c0)

3. The program will suggest an optimized route of visit.

![Optimized Route](https://github.com/EthanLawyer/5800-Final-Project/assets/133042033/6d7a5ece-d1c2-4b4f-a3d6-2f05d2f4a93a)
