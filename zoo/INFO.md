Problem Statement: Write a Python program that defines an Animal base class with an eat() method, creates a few subclasses with their own eat() implementations, and builds a Zoo class that holds a list of animals and calls eat() on all of them via a feed_all() method.

Purpose: This exercise combines composition with polymorphism. The Zoo class does not need to know the specific type of each animal; it simply calls the shared eat() interface on every object in its collection, and each animal responds in its own way.

Given Input: A zoo containing a Lion, a Elephant, and a Parrot