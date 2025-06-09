let previous = 1
let fibonacci = 1

const doRecursiveThings = () => {
    // update fibonacci to the next value in the sequence
    let new_previous = fibonacci
    fibonacci += previous
    previous = new_previous
    console.log("Current sequence value:", fibonacci)
    if (fibonacci < 1000000000){
        doRecursiveThings()
    }
}

doRecursiveThings()

function sort() {
    let sorted = false
    // do sorting stuff

    // check if sorted
    if(!sorted){
        sort()
    }
}