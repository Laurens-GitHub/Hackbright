// Python:
// def print_indices(items):
//     """Print each item in the list, followed by its index.

//     The output should look like this:
//         apple 0
//         berry 1
//         cherry 2

//     Arguments:
//         items (list)

//     Returns:
//         None
//     """

//     for i in range(len(items)):
//         print(f'{items[i]} {i}')


// Translation
'use strict';

// 1. printIndices
function printIndices(items) {

  for (const item of items) {
    console.log(`${item} ${items[item]}`);

  }
}


//Python
// def every_other_item(items):
//     """Print a list of every other item in `items`

//     Start with index 0.

//     Arguments:
//         items (list)
//     """

//     result = []

//     for i in range(len(items)):
//         if i % 2 == 0:
//             result.append(items[i])

//     print(result)

// Translate:
// 2. everyOtherItem
function everyOtherItem(items) {
  // Replace this with your code
  const result = [];

    for (const item of items.slice(0, items.length)) {
      if (num % 2 === 0) {
        result.push(item);
      }
    }
  console.log(result);
  }

// 3. smallestNItems
function smallestNItems(items, n) {
  const result = [];
  const sortedList = items.sort;
  result.push(sortedList.slice(n));
  return result;
}
