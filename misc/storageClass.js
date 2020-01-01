/*

Create a class called Storage

Add functionality to Storage in the following ways:

1) Create a method called addThing that accepts one argument.  When addThing is called, the argument is added to storage:

const myStorage = new Storage();

myStorage.addThing("CSS");
myStorage.addThing("JS");
myStorage.addThing("CSS");

2) Calling getThings() will log everything currently in storage:
myStorage.getThings(); // ["CSS", "JS", "CSS"]

3) addThing should have one more behavior: after the argument is added to storage, return a remove function.  If you call remove(), the argument that was added is removed from the list:

const myStorage = new Storage();

const removeCSS = myStorage.addThing("CSS");
const removeJS = myStorage.addThing("JS");
const removeSecondCSS = myStorage.addThing("CSS");
myStorage.getThings(); // ["CSS", "JS", "CSS"]

removeCSS();
myStorage.getThings(); // ["JS", "CSS"]

*/

class Storage {
  constructor() {
    this.state = [];
    this.lastId = 1;
  }

  getId() {
    return this.lastId++;
  }

  addThing(thing) {
    const id = this.getId();
    this.state.push({ val: thing, id });
    return () => (this.state = this.state.filter(thing => thing.id !== id));
  }

  getThings() {
    console.log(this.state.map(thing => thing.val));
  }
}

//Test Solutions, feel free to expand
const myStorage = new Storage();
const removeX = myStorage.addThing('X');
const removeXX = myStorage.addThing('XX');
const removeY = myStorage.addThing('Y');
const removeYY = myStorage.addThing('YY');
const remove1 = myStorage.addThing('1');
const remove2 = myStorage.addThing('2');
const removeSecondYY = myStorage.addThing('YY');
const remove3 = myStorage.addThing('3');
const removeSecondX = myStorage.addThing('X');
myStorage.getThings(); // [ 'X', 'XX', 'Y', 'YY', '1', '2', 'YY', '3', 'X' ]

removeX();
removeSecondX();
myStorage.getThings(); // [ 'XX', 'Y', 'YY', '1', '2', 'YY', '3' ]

removeSecondYY();
myStorage.getThings(); // [ 'XX', 'Y', 'YY', '1', '2', '3' ]
