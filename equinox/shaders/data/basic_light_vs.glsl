  #version 330
in layout(location = 0) vec3 inPosition;
in layout(location = 1) vec3 inNormal;

out vec3 Normal;
out vec3 FragPos;  

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectMatrix;




void main()
{
    gl_Position = projectMatrix*viewMatrix*modelMatrix*vec4(inPosition,1.0f);
    FragPos = vec3(modelMatrix * vec4(inPosition, 1.0));
    Normal = mat3(transpose(inverse(modelMatrix))) *inNormal;
}