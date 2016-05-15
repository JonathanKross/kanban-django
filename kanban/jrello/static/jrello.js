var $tasks = $('#tasks');

// $.getJSON('http://localhost:8000/api/jrello', function(tasks){
//   tasks.results.forEach(function(tasks) {
//     console.log(tasks)
//     var $li = $('<li>');
//     $li.text(jrello.title)
//     $li.appendTo($tasks);
//   })
// })



var $task = $('#task');
var $title = $('input[name="title"]');
var $description = $('input[name="description"]');
var $priority = $('input[name="priority"]');
var $is_completed = $('input[name="is_completed"]');

$task.submit(function() {
  console.log('you submitted the form');

  $.ajax({
    method: 'post',
    url: 'http://127.0.0.1:8000/api/jrello/',
    // username: 'admin',
    // password: 'password123',
    dataType: 'json',
    processData: true,
    data: {
      title: $title.val(),
      description: $description.val(),
      priority: $priority.val(),
      is_completed: $is_completed.val()
    },
    success: function(newTask) {
      console.log(newTask)
      var $li = $('<li>');
      $li.text(newTask.name)
      $li.appendTo($tasks);
    }
  });

  return false;
});
