DSA
Day3

In C, C++

have compiler, the compiler takes the entire .c,.cpp file and convert it in to machine code.

But In Java 
have compiler, which convert .java(source file) into byte code(.class file)
for running this .class file, we need JVM(java virtual machine).
then the interpreter line by line convert that byte code into machine code.

why platform independence?
 - the byte code can run on all operating system. eg: if i developed a code in mac and compiled then the .class can run on Linux, windows

- in c, c++ compiler convert directly it into .exe (machine code), which cannot be run on other os, if we want to run it, again compile the code, the compiler convert code to corresponding os machine code.

how we run the java byte  code in all OS?

with the help of JVM. we can run byte code using JVM and convert it into machine code.
But JVM is platform dependent, java is platform independent.

qn: JVM perform same job as compiler of c, cpp then why we need JVM. if we want to run code we just compile it, why we use JVM in the middle , is there any need?


JDK(Java Development kit)

if we want to develop and run a java program JDK is require
it's a package of files contains:
    -development tools : to provide environment to develop your program
    -JRE - to execute the program
    -compiler - javac
    -archiver - jar
    - doc generator - Javadoc
    - interpreter/ loader
JRE(Java runtime environment)
	- installation package only run the program
	-consists of:
		1. deployment technologies
		2. UI toolkit
		3.Integration libraries
		4.base libraries
		5.JVM
	-after we get .class file , the next things happen at runtime:
		- Loading :class loader loads all classes needs to execute the program: 
			* read the .class file and generate it binary data
			* an object of this class is created in the heap
		- Linking: JVM sends code to byte code verifier to verify the format of the code:
			* jvm verify .class file
			* allocate memory for class variables and default values.
			* replace symbolic references from the type with direct references.
		-Initialization:
			* all static variables are assigned with their values defined in the code and static block

JVM contains the stack and heap memory allocations.

JVM execution
Interpreter:
	-Line by line execution
	- when one method is called many times, it will interpret again and again.
JIT :
	- those methods that are repeated, JIT provides direct machine code so re-interpretation is not required
	- make execution faster
garbage collector(JVM GC) : identify and free up memory that is no longer being used by the program. so it can be reused. preventing memory leaks and improving performance.

 ---------------------------------------------------------END-----------------------------------------------------------------------