/* this module is for research purposes. the project will contain a fetch to a n API
to better learn this concept*/

fetch("https://example.com/api/data")
.then(response => response.json()) //response is parsed from a response
.then(data => {
    console.log(data); //prints the data parsed
})
.catch(error => {
    console.log(error); //handles any error
});

/* the following snippet is for handling post requests */

fetch("http://localhost:5000/api/v1/login", { //we nest objects within a fetch
    method: "POST", //the crud method being performed
    headers: {
        'content-type': 'application/json' //header extension from the curl command
    },
    body: JSON.stringify({ //creates an object of the credentials that we will insert
        username: 'Kevin', //all of this is very reminiscent of working with cURL
        password: 'secret123' //where we load the data as a JSON
    })                        // object with the -d option
})
.then(response => response.json())
.then(data => {
    if (data.success) {
        console.log('Login Successful')
    } else {
        console.log('Login failed:', data.message)
    }
})
.catch(error => {
    console.log(error)
})


/*real life now. We will use the jsonplaceholder file to retrieve information */

fetch("https://jsonplaceholder.typicode.com/posts/1")
.then(response => response.json()) //again, this retrieves data
.then(post => {
    console.log(`Post title: ${post.title}`); //data contained is JSON object
    document.querySelector('.action').textContent = post.title; //so we can implement key, value searches
})

/* now that we have established the basics, its time to integrate asynchronous functions 
as established, async functions are functions that perform and do not stop every other
operation if the expected response or return did not make it. It instead wait until it
is needed by the method calling it*/
async function loadUser() {
    try{
        const response = await fetch("api/user");
        const data = await response.json();
        console.log(data);
    }
    catch(err){
        console.error("Foound an error:", err)
    }
}

loadUser()


/* task: fetch two things:
1) get a post
2) get a user */

async function loadPostAndUser() {
  try {
    const postRes = await fetch('https://jsonplaceholder.typicode.com/posts/1');
    const post = await postRes.json();

    const userRes = await fetch(`https://jsonplaceholder.typicode.com/users/${post}`);
    const users = await userRes.json();
    console.log("Post title:", post.title);
    console.log("Post user:", users.name)
    } catch(err) {
        console.error("Failed to load post or user", err);
    }
}

loadPostAndUser()

async function postingFromApi() {
    const button = document.getElementById('load-post');
    const header = document.getElementById('post-title');
    const para = document.getElementById('post-body');
    const new_list = document.getElementById('post-list');

    button.addEventListener('click', async () => {
        const postRe = await fetch('https://jsonplaceholder.typicode.com/posts/2')
        const new_post = await postRe.json();
        header.textContent = new_post.title;
        para.textContent = new_post.body;
    })

    button.addEventListener('click', async() => {
        const allPostRe = await fetch('https://placeholder.typicode.com/posts');
        const posts = await allPostRe.json();

        new_list.innerHTML = ''; //creates an empty element

        for (const post of posts.slice(0, 5)) {
            const li = document.createElement('li') //creates a new element in the HTML
            li.textContent = post.title; //writes the content in the newly created tag
            new_list.appendChild(li); //appends the li elements to the list
        }
    })
}

postingFromApi()
