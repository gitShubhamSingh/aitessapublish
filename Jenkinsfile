pipeline {
		agent any
		stages{
	        stage("cloneCode"){
	            steps {
	                echo "Cloning the code"
	                git url:"https://github.com/gitShubhamSingh/aitessapublish.git",branch:"main"
                }
            }
            stage("build"){
	            steps {
	                echo "Building the image"
	                sh "docker build -t aitessa-app ."
                }
            }
            stage("pushToDockerHub"){
	            steps {
	                echo "Pushing the image to Docker hub"
	                withCredentials(
	                    [
	                        usernamePassword(
	                            credentialsId:"dockerHub", 
	                            passwordVariable:"dockerHubPass", 
	                            usernameVariable:"dockerHubUser"
	                       )
	                   ]
	               ){
	                   sh "docker tag aitessa-app ${env.dockerHubUser}/aitessa-app:latest"
	                   sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
	                   sh "docker push ${env.dockerHubUser}/aitessa-app:latest"
	               }
                }
            }
            stage("deploy"){
	            steps {
	                echo "Deploying the container"
	                sh "docker-compose down && docker-compose up -d"
                }
            }
	   stage("deletingUnusedDockerImage"){
		steps{
			echo "Flushing the unused container"
			sh "docker image prune -a"
		}	
	   }
        }
    }
