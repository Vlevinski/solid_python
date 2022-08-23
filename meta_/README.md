The term metaprogramming refers to the potential for a program to have knowledge of or manipulate itself. Python supports a form of metaprogramming for classes called metaclasses.

Metaclasses are an esoteric OOP concept, lurking behind virtually all Python code. You are using them whether you are aware of it or not. For the most part, you don’t need to be aware of it. Most Python programmers rarely, if ever, have to think about metaclasses.

When the need arises, however, Python provides a capability that not all object-oriented languages support: you can get under the hood and define custom metaclasses. The use of custom metaclasses is somewhat controversial, as suggested by the following quote from Tim Peters, the Python guru who authored the Zen of Python:

    “Metaclasses are deeper magic than 99% of users should ever worry about.
    If you wonder whether you need them, you don’t (the people who actually need 
    them know with certainty that they need them, and don’t need an explanation 
    about why).”

    — Tim Peters

There are Pythonistas (as Python aficionados are known) who believe that you should never use custom metaclasses. That might be going a bit far, but it is probably true that custom metaclasses mostly aren’t necessary. If it isn’t pretty obvious that a problem calls for them, then it will probably be cleaner and more readable if solved in a simpler way.

Still, understanding Python metaclasses is worthwhile, because it leads to a better understanding of the internals of Python classes in general. You never know: you may one day find yourself in one of those situations where you just know that a custom metaclass is what you want.