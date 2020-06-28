# task-catalog-poc
Task catalog POC

This repository is a POC (Proof of Concept) of the idea to have a catalog of common methods shared by multiple executors (clients) with two main features.

## Method versioning

One method may have multiple versions wich the executors can select on runtime.

## Method plugability

A method my also have one or more plugin points to add extra bits of custom behaviour

## Technology

The aim is to create a good POC without using any framework or library besides the Python standard library

This project is being developed with Python 3.8 in mind, but any version of python from 3.6 onwards should work fine.

## How does it work

To define an 'interface' that is, a method that is both versioned and allows for plug-ins we need to perform the following steps:

* Create a new file the interface name in `src/interfaces/`

    For example: `interface_a.py`

* The file should have at least one method called `<interface_name>_entrypoint_v<version>`

    For example: `interface_a_entrypoint_v1`

    All interface entrypoints should have at least two arguments:

    * `ctx`: Execution context, needed for plugin identification
    * `**kwargs`: Extra arguments that may be optional

    The minimum version expected is 1.

* For plugin creation we need to define a new 'customer' folder in the `src/plugins` folder or reuse an existing one.

    For example: `src/plugins/customer_1/`

* Inside the 'customer' folder we need to add a file with the same name as the interface we intend to add plugins for.

    For example: `customer_1/interface_a.py`

* Inside the file we will define all plugins for `customer_1` targeting `interface_a`.

    In order for the plugin to be recognized it needs to be decorated with the `plugin_config` decorator.

    Plugin methods only have two parameters: `ctx` and `**kwargs`.

## TODO

* Define a configuration format so that an interface can properly define what type of plugins go to each plugin slot.

    For example: plugin arguments, plugin return values

* Better logging integration

* Better exception handling
