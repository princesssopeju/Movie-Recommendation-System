## Project Title: **Movie Recommendation System**

### Project Overview:
The Movie Recommendation System is a web-based application that suggests top-rated movies to users based on their selected genre and recency preference (all-time or recent). The project was developed using Flask as the web framework and deployed on an AWS EC2 instance. The system processes movie ratings data to generate recommendations, making it a practical application of data analysis and web development skills.

### Key Features:
- **Genre-Based Recommendations:** Users can select a genre to get the top 10 movies within that genre.
- **Recency Filter:** Users can choose to view all-time top-rated movies or movies from the last 10 years.
- **User Interface:** A simple and intuitive interface where users can select genres and view recommended movies.
### Screenshots
![Screenshot 2024-08-15 210810](https://github.com/user-attachments/assets/43e0ee6e-cfa7-49f4-8d87-07050f31d591) 


## DEMO


https://github.com/user-attachments/assets/9a5e1e89-05b2-45b6-9c23-cba9531a3a63




### Technologies Used:
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS (for styling the web pages)
- **Data Processing:** Pandas (Python library)
- **Deployment:** Initially set up on AWS EC2, with explorations into using AWS Lambda and Zappa for serverless deployment.
- **Data Storage:** The movie data was initially stored and processed locally, then explored with S3 bucket integration for scalability.

### Steps and Progress:
1. **Initial Setup:**
   - Flask app initialized with basic routing.
   - Loaded and processed movie ratings and metadata using Pandas.
   - Implemented a recommendation logic based on genre and recency.

2. **Front-End Development:**
   - Created `index.html` and `results.html` templates to provide a user-friendly interface.
   - Implemented a card-based layout to display movie recommendations.
   - Added CSS for better styling and user experience.

3. **Testing and Validation:**
   - Tested the application locally with various genres and recency filters.
   - Debugged issues related to specific genres (e.g., 'Sci-Fi' was labeled as 'Science Fiction' in the data).
   - Refined the recommendation logic to handle cases where no movies were found for certain filters.

4. **Deployment Attempts:**
   - Initially deployed on AWS EC2 using Flask’s development server.
   - Explored deploying the app using Zappa to AWS Lambda, which encountered challenges related to environment setup and S3 integration.
   - Decided to keep the deployment on AWS EC2 due to simplicity and the project’s current needs.

5. **Final Adjustments:**
   - Cleaned up the project files and ensured everything runs smoothly on the EC2 instance.
   - Recorded a demo of the project in action for portfolio purposes.

### Challenges and Learnings:
- **Data Handling:** Managing large datasets efficiently on limited resources, leading to the decision to process subsets of data (e.g., 2 million rows).
- **Deployment Complexity:** The complexities of serverless deployment with Zappa, especially related to dependencies and environment variables.
- **User Interface Design:** Balancing functionality and user experience, especially in presenting data (e.g., using cards for movie listings).

### Future Enhancements:
- **Scalability:** Consider implementing more efficient data storage and retrieval mechanisms for larger datasets.
- **Deployment Optimization:** Revisiting serverless deployment with a more streamlined setup or exploring containerization with Docker.
- **User Interface Improvements:** Adding features like movie posters, search filters, or even user reviews.
