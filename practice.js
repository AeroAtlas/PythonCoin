var names = ["Bob", "Bill", "Jill"]

function doSomething() {
  for(name in names){
    console.log(name.length)
  }
}
doSomething()