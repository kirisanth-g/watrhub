# watrhub

WatrHub Take Home Problem:



You are the operator of a water company whose job is to maximize the water drainage of a polluted lake while minimizing the cost to do so. The way the company does this is by draining the lake into a truck for one hour at a time. This specialized truck can have any number of pipes attached to it and also has a capacity given in litres. The company must select the optimal set of pipes to attach to the truck to maximize the drainage each hour, while minimizing cost.



Input is given in the following JSON format:
```
input = {

      truck: capacity_in_litres
      pipes: [
            {
              name: n1,

              cost: c1,

              litres: l1 // how much can get drained in one hour

            },
            {
                name: n2,
                cost: c2,
                litres: l2
            },
            ...
      ]
}
```


Output:
```
Pipes: optimal_pipe_n1, optimal_pipe_n2, ... optimal_pipe_nN

Cost: cost to optimally fill
```

Note: *** It is not necessary that the truck is filled to the top. ***

Example input:
```
input = {
      truck: 60
      pipes: [
          {
              name: 'pipe 1',
              cost: 10,
              litres: 20
          },
          {
              name: 'pipe 2',
              cost: 15,
              litres: 50
          },
          {
              name: 'pipe 3',
              cost: 4,
              litres: 25
          },
          {
              name: 'pipe 4',
              cost: 11,
              litres: 30
          }
    ]
}
```

Example output:
```
Pipes: pipe 3, pipe 4

Cost: 15
```
