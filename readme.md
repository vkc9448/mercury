```yaml
milestone:
    iteration: 05
    title: "Performance and Refactoring"
    date: "April 9, 2021"
group:
    number: 06
    name: "Mercury- The Data Delivery System"
    members:
    - "Vincent Cheng"
    - "Dishant Mishra"
```  
  
# Mercury - The Data Delivery System
## Project Requirement
- 24/7 Shared Server
- Relational Database 
- API Queries
- Object-Oriented Programming Language 

## Performance

We have opted to go with python in this rewrite as this gives us access to FastAPI, 
a library written almost entirely with speed in mind. It has it's internals written 
in highly optimized C. It also supports asynchronization out of the box, which makes 
it really appealing for handling high traffic on highly used endpoints for the API.

Another reason is the fact that allows us to strongly type (I know I say that as I 
use a duck-typed language) body and query parameters for the requests. 

Another decision we made was use the non-standard asyncpg drivers to interact 
with postgres. This driver is also highly optimized as it has its internals written in 
Cython. This library allows us to use raw SQL asynchronously which is good for 
optimizing reads. 

## Design

One of the benefits of going with FastAPI is that it is design agnostic. This allows us
to use any design pattern we desire to organize our project. We decided to go with 
an MVCesque domain-based patter where our routing is separate from our models and 
controllers, which is desirable for modularity.

The project rewrite is allowing us to use postgres from the start with a high 
performance specialized driver. Something that we were not able to find a good 
replacement for in nodejs without using an orm based driver.
