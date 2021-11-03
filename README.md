# Practica6_sistemas_inteligentes
## Members

- Daniel Camacho

## 1. Describing the Problem
This is a problem of Pssr this mean that I have  to define  a set of variables, set of constraints, define the domain that can be assigned to each variable and then implement the backtrack/backjump algorigthm to find the solution. In both algorithms the idea is the same first we have to check if the assignation of all nodes is complete if it is true we just have to send it back, then if it is not true we pick an unsigned variable here we use the Most Constrained Value algorithm that consists of pick the variable which has the shortest quantity of consistents values in his domain, after pick the variable we have to sort the values in the domain of the picked variable, for do that we use the Less constrained value algorithm which is about the opposite of Most Constrainde Value this means that we have to sort the domain values of the variable that we pick for the number of consistent valus of the domain variables of the nieghbours in decreasing order. then for each value in the domain of the picked variable we have to verify that this value fullfill the restrictions or constraints that the problem define. if not fulfill the constraints then we just continue to the next valude in the domain of the variable picked, and if it fulfill we just update the domains of the rest of the variable, for do that we can use 2 algorithms, the first one is Forward Checking which consist of after give the value at the variable, check the domain of the neighbours and delete the inconsistent values and the second one is Arc Consistency that is similar but the diference is that we dont just update the domain of the neighbouts, beside of do that we updete the domains of the neighbours of the neighbours.... and finally after do all that just do that process again with other variable.
In the problem we have to find a way that can help "Universidad Catolica" to organize his speakers for his event, to do that they give us the category of each conference that is:
- Informatic Security
- Software Enginering
- Artificial intelligence

Also they give us a set of constraint for each speaker, and the date and hour and duration of each conference

## 2. Describing the Solution
For solving the problem firstly i define:
- Set Variables: Each daily schedule in the total of duration off the event.
- Set of domain: The domains are a list of speakers for each category.
- Assignations: Each daily schedule is going to have list os speakers that will do the conference at that schedule
- Constraints:
    - One speaker can give 5 conference in the same cateogry but cant give two conference in a row 
    - Two speaker of the same category cant be assigned in the same schedules. Two speaker of different category can be assigned in the same schedules
    - The speakers give the day and the hour of his preference to do the conference
    - Two international speakers cant be assigned in the same schedule
    - The schedules can be withous a speaker, this depends in the quantity of speakers

Then after do all the definitions we have to implement the bactrack algorithm, i start coding that in main.py with the basic algorithm and coding the set of definitions.
I start defining the classes (it can see it in /images/Class_diagram), the nodes will be the schedules and the domain will be the speakers. Each node can have a set of speakers in his value and a list of list of speakers in his domain, that was the moment when i realized that i was doing a bad focus, so after thinking a lot i redifined my concepts:

- Set Variables: Each variable is the single Node that is defined by his daily schedule and the category of the conference, it can see it better in the diagram that i made in /images/Redifined_single_node_diagram, then i realized that this new focus will be better because now a node have just  single value that is the speaker and not a list of values like in the other focus. The complete node diagram can see it in /images/redifined_node_diagram
- Set of domain: Now the domain are the list of all speakers each one  with his own characteristics that is specified in his class diagram, For coding that and to make it easier i define that if a speaker gives more than a conference i will add it like other speaker, at the end i will have a list of speakers each one with a single conference, so if a speaker is going to do 3 conference the speaker will appear 3 times in the domain each one with his own preference day and hour.
- Assignations: Each single Node is going to have a single speaker of a single category with an unique conference.
- Constraints:
    - The speakers only will do the conference is his preference day and his preference hour is available, else it will be consider like an inconsistent state.
    - One speaker cant give two conference in a row
    - Two speakers of the same category cant be assigne in the same hour
    - Two international speakers cant be assigned in the same hour
    - The schedules can be without a speaker, this depends in the quantity of speakers

Then after redined all the definitions i start to change my code to this new version that i'm sure that will work, in order to do that i made my new class diagram (/images/redifined_class_diagram), the solution is in singleCategory.py file.

I start to make my automated domain generator, to make it easy the test. Is really important understand that i will going to have a domain of speakers with only a conference, but can appear up to 5 times in it, once i made that i generate my list of nodes(variables), i give all them a value in his day and hour, and make the relations beetwen his neighbours. Then i implement the backtrack algorithm with each of his parts

Starting checking when an assignation is complete, in this case an assignation will be completed if all the nodes(a unique conference with an unique category, day and hour ) have a speaker or if all the speakers are assigned to do a conference.

Then i continue developing the Mostr Constrained algorithm, in this section i pick the node with the less quantity of consistent values, to do that firstly i visit each node and give a priority in base of the quantity of preference day and hour that speakers has in this node, i do that because if i didnt do that there is the posibility to pick an hour where any speaker want to make his conference, this means that will not pass the constraint, once i give this priority i sort them in base of the quantity of consistent values.

Then i start to develop the Least constrained value, this is for sorting the domain of the node that i pick, in base of the quantity of consistent values that the neighbours nodes has if i assigned each value to the picked node, once i sort the domain i send that to the next part.

I iterate each speaker in the sorted list and i check if the possible speaker assigned fulfill the restrictions, if it isnt i iterate to the next one and if it is i assign the speaker to the node and upgrade the domain of the neigbour nodes with the Forward Checking algorithm

Finally i call again the backtrak function with the new list of nodes updated and repeat the process
## 3. Experiments & Results

I start defining the list of the domain with a lot of speakers and then with few speakers, the results are similar, basically depends if the speakers hasnt the same hour, day and category, if it hasnt then the solution is possible

## 4. Conclusions

The problem depend completely in the speakers preference hour and day, if a speakers cant give a conference in his prefence day or hour then it is an inconsisten asignement, the solution is found with this new way to solve the problems but it consume a lot of space to do that, it focus only in resolve it not in how.

### Comments


## 5. Bibliography


➡️  HeapQ: [Docs Python][heapq]
➡️  CopyLists: [Docs Python][copy]
➡️  HeapQ_Objects: [StackOverflow][lessthan]
➡️  Random: [PythonDocs][random]


[heapq]: https://docs.python.org/3/library/heapq.html
[copy]: https://docs.python.org/3/library/copy.html?highlight=copy#module-copy
[lessthan]: https://stackoverflow.com/questions/49277168/issue-using-heapq-in-python-for-a-priority-list
[random]: https://docs.python.org/3/library/random.html#random.randrange