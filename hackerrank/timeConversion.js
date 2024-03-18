function timeConversion(s) {
  //takes the AM/PM postifx off
  let finalResult = s.slice(0, -2);
  //initialize hour to first two chars, only change if needed
  let hour = s.slice(0, 2);
  //if it is AM and 12, the hour is 00. special case.
  if (s[8] === 'A' && s[0] + s[1] === '12') {
    hour = '00';
    finalResult = hour + s.slice(2, -2);
    //otherwise, if it's PM and the hour is > 12, add the hour to 12
  } else if (s[8] === 'P' && s[0] + s[1] !== '12') {
    //add the hour to the front of the string, replacing the old hour
    const numVer = Number(s[0] + s[1]);
    hour = String(numVer + 12);
    finalResult = hour + s.slice(2, -2);
  }
  //whether or not the hour had to be changed, return the final result
  return finalResult;
}

console.log(timeConversion('07:05:45PM'));
console.log(timeConversion('12:00:45AM'));

/* 
Given a time in

-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock. 

Input Format

A single string
that represents a time in -hour clock format (i.e.: or ).
*/
