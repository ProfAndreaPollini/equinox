#version 330
            
out vec4 outColor;

void main()
{
    vec3 objectColor = vec3(0.0,1.0,0.0);
    vec3 ambientLightColor= vec3(1.0,0.0,0.0);
    float ambientLightStrenght = 0.8;

    vec3 ambientLight = ambientLightStrenght*ambientLightColor;
    vec3 color = ambientLight * objectColor;
    outColor = vec4(objectColor,1.0);
    
}