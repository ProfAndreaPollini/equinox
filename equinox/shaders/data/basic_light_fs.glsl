#version 330
in vec3 Normal;
in vec3 FragPos;  

out vec4 outColor;

uniform vec3 objectColor;
uniform vec3 lightPos;
uniform vec3 viewPos;

void main()
{
    float specularStrength = 0.9;
    
    //vec3 objectColor = vec3(0.5,1.0,0.5);
    vec3 ambientLightColor= vec3(1.0,1.0,1.0);
    vec3 lightColor= vec3(1.0,1.0,1.0);
    float ambientLightStrenght = 0.6;
    //vec3 lightPos = vec3(0.0,0.0,2.0);

    vec3 ambientLight = ambientLightStrenght*ambientLightColor;
    vec3 color = ambientLight * objectColor;

    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(lightPos - FragPos);  

    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuseLight = diff * ambientLightColor;
    

    vec3 viewDir = normalize(viewPos - FragPos);
    vec3 reflectDir = reflect(-lightDir, norm);  
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32);
    vec3 specular = specularStrength * spec * lightColor; 


    vec3 result = (color + diffuseLight + specular) * objectColor;

    outColor = vec4(result, 1.0);  
    
    
}