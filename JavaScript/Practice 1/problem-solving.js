const evenOrOdd = (num) => {
  if (num % 2) console.log("Even");
  else console.log("Odd");
};

const sortNum = (arr) => {
  arr.sort((a, b) => a - b);
  return arr;
};

const isLeapYear = (year) => year % 400 == 0 || (year % 4 == 0 && year % 100);

const numDivBy3N5 = () => {
  let arr = [];
  for (let i = 1; i <= 50; i++) if (i % 3 == 0 || i % 5 == 0) arr.push(i);
  return arr;
};

var friends = ["rahim", "karim", "abdul", "sadsd", "heroAlom"];
const longestName = (names) => {
  let result = "";
  names.forEach((name) => {
    if (result.length < name.length) result = name;
  });
  return result;
};

console.log(longestName(friends));

var numbers = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10];
const removeDup = (arr) => {
  const res = [];
  for (let val of new Set(arr)) res.push(val);
  return res;
};

removeDup(numbers);

const biggestNum = (arr) => {
  let res = 0;
  for (let i = 0; i < arr.length; i++) if (arr[i] > res) res = arr[i];
  return res;
};

const monthlySavings = (allPayments, livingCost) => {
  if (!Array.isArray(allPayments) || typeof livingCost != 'number') return "Invalid Input";

  let tax = 0;
  allPayments.forEach((payments) => {
    if (payments >= 3000) tax += (payments * 10) / 100;
  });

  let = savings = allPayments.reduce((acc, curr) => acc + curr, 0);

  if (savings < tax + livingCost) return "Earn More";

  return savings - tax + livingCost;
};

let payments = [1000, 3000, 5000, 5000], livingCost = 5000;
console.log(monthlySavings(payments, livingCost))