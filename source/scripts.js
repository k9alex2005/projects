document.addEventListener('DOMContentLoaded', function () {

    listCourses = document.querySelector('.list-of-courses ul');
    currentCourse = document.getElementById('learning');

    index = 0;
    currentCourses = ['Artificial Intelligence', 'Web application Development',
        'Operating Systems', 'Database Systems'
    ]


    //every 3 seconds showcase a new subject that is currently being learned
    setInterval(() => {

        currentCourse.textContent = currentCourses[index];
        console.log(index);
        index = (index + 1) % currentCourses.length;

    }, 3000);


    //event to give a brief description about a particular course when clicked
    //and to remove description when clicked again
    function courseDesc(event) {
        courseItem = event.target;


        let showCurrent = courseItem.children[0].style.display
        console.log(showCurrent);
        if (showCurrent == "") {
            courseItem.children[0].style.display = 'block'
        }
        else {
            courseItem.children[0].style.display = '';
        }
    }
    listCourses.addEventListener('click', courseDesc)

});




