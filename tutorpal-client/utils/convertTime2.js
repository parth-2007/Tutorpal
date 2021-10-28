function convertTime2(time){
  const date = (time || '').substring(0, 10)
  let times = (time || '').substring(11, 16)

  times = (times || '').toString().match(/^([01]\d|2[0-3])(:)([0-5]\d)(:[0-5]\d)?$/) || [time];
 
  if (times.length > 1) { // If time format correct
    times = times.slice(1); // Remove full string match value
    times[5] = +times[0] < 12 ? ' AM' : ' PM'; // Set AM/PM
    times[0] = +times[0] % 12 || 12; // Adjust hours
  }
  times = times.join('')
  return times+"・" + date;
}

export default convertTime2