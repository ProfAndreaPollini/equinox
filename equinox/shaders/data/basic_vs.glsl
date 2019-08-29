  #version 330
in layout(location = 0) vec3 position;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectMatrix;

void main()
{
    gl_Position = projectMatrix*viewMatrix*modelMatrix*vec4(position,1.0f);
}