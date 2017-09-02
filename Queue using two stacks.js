https://www.hackerrank.com/challenges/queue-using-two-stacks?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=15-day-campaign

function processData(input) {
    //Enter your code here
    input =input.split('\n');
    var queue = [];
    for (i=1; i<= input[0];i++){
        let val = input[i].split(' ');
        switch(val[0]) {
            case '1':
                queue.push(val[1]);
            break;
            case '2':
                queue = queue.slice(1);
            break;
            
            case '3':
                console.log(queue[0])
            break;
        }
    }
} 