var app = new Framework7({
  // App root element
  root: '#app',
  // App Name
  name: 'My App',
  // App id
  id: 'com.myapp.test',
  // Enable swipe panel
  panel: {
    swipe: 'left',
  },
  // Add default routes
  routes: [
    {
      path: '/register/',
      url: 'register.html',
    },
    {
      path: '/login/',
      url: 'login.html',
    },
  ],
  // ... other parameters
});

var mainView = app.views.create('.view-main');

var $$ = Dom7;

 myApp.alert('Here comes About page');