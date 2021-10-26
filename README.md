# Practica6_sistemas_inteligentes
## Members

- Daniel Camacho

## 1. Describing the Problem
This is a problem of Pssr this mean that I have  to define  a set of variables, set of constraints, define the domain that can be assigned to each variable and then implement the backtrack/bakcjump algorigthm to find the solution.In both algorithms the idea is the same first we have to check if the assignation of all nodes is complete if it is true we just have to send it back, then if it is not true we pick an unsigned variable here we use the Most Constrained Value algorithm that consists of pick the variable which has the shortest quantity of consistents values in his domain, after pick the variable we have to sort the values in the domain of the picked variable, for do that we use the Less constrained value algorithm which is about the opposite of Most Constrainde Value this means that we have to sort the domain values of the variable that we pick for the number of consistent valus of the domain variables of the nieghbours in decreasing order. then for each value in the domain of the picked variable we have to verify that this value fullfill the restrictions or constraints that the problem define. if not fulfill the constraints then we just continue to the next valude in the domain of the variable picked, and if it fulfill we just update the domains of the rest of the variable, for do that we can use 2 algorithms, the first one is Forward Checking which consist of after give the value at the variable, check the domain of the neighbours and delete the inconsistent values and the second one is Arc Consistency that is similar but the diference is that we dont just update the domain of the neighbouts, beside of do that we updete the domains of the neighbours of the neighbours.... and finally after do all that just do that process again with other variable.
In the problem we have to find a way that can help "Universidad Catolica" to organize his speakers for his event, to do that they give us the category of each conference that is:
    - Informatic Security
    - Software Enginering
    - Artificial intelligence
Also they give us a set of constraint for each speaker, and the date and hour and duration of each conference

## 2. Describing the Solution
For solving the problem i define:
    - Set Variables: Each daily schedule in the total of duration off the event.
    - Set of domain: The domains are a list of speakers for each category.
    - Assignations: Each daily schedule is going to have list os speakers that will do the conference at that schedule
    - Constraints:
        • One speaker can give 5 conference in the same cateogry but cant give two conference in a row 
        • Two speaker of the same category cant be assigned in the same schedules. Two speaker of different category can be assigned in the same schedules
        • The speakers give the day and the hour of his preference to do the conference
        • Two international speakers cant be assigned in the same schedule
        • The schedules can be withous a speaker, this depends in the quantity of speakers
## 3. Experiments & Results

## 4. Conclusions

### Comments


## 5. Bibliography


➡️  HeapQ: [Docs Python][heapq]
➡️  CopyLists: [Docs Python][copy]

[heapq]: https://docs.python.org/3/library/heapq.html
[copy]: https://docs.python.org/3/library/copy.html?highlight=copy#module-copy