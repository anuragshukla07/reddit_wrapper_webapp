const articlesContainer = document.getElementById('articles');

fetch('/articles/')
    .then(response => response.json())
    .then(articles => {
        articles.forEach(article => {
            const articleElement = document.createElement('div');
            articleElement.className = 'article';
            articleElement.innerHTML = `
                <h2>${article.title}</h2>
                <p>Author: ${article.author}</p>
                <p>Creation Date: ${new Date(article.creation_date * 1000)}</p>
                <a href="${article.link}" target="_blank">Read More</a>
            `;
            articlesContainer.appendChild(articleElement);
        });
    });
