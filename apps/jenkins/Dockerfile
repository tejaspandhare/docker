FROM jenkins/jenkins:lts
USER root
RUN apt-get update && \
    apt-get install -y \
        software-properties-common \
        ansible \
        sudo \
    && apt dist-upgrade -y \
    && apt-get clean
RUN echo "jenkins ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/jenkins
WORKDIR /usr/share/jenkins
RUN curl -L -o jenkins.war https://get.jenkins.io/war/latest/jenkins.war
EXPOSE 8080
EXPOSE 50000
USER jenkins
