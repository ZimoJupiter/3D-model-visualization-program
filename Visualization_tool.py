"""
@ A small tool for 3D visualization with an simple eVTOL model
@ author ZimoJupiter
@ w.zimo@outlook.com
@ date 18 Dec 2024
@ license MIT License
"""
import vtk
import pandas as pd
import numpy as np

renderer = vtk.vtkRenderer()
renderer.SetBackground(1,1,1)
# renderer.GradientBackgroundOn()
window = vtk.vtkRenderWindow()
window. AddRenderer(renderer)
window.SetSize (3200, 2400)
interactor = vtk.vtkRenderWindowInteractor( )
interactor. SetRenderWindow ( window )
interactor.SetInteractorStyle( vtk.vtkInteractorStyleTrackballCamera())

stlReader1 = vtk. vtkSTLReader()
stlReader1.SetFileName( "3D models/eVTOL.stl" )
filter1 = vtk. vtkOutlineFilter()
filter1. SetInputConnection( stlReader1.GetOutputPort( ))
outLineMapper1 = vtk. vtkPolyDataMapper()
outLineMapper1.SetInputConnection(filter1. GetOutputPort( ))
stlMapper1 = vtk. vtkPolyDataMapper()
stlMapper1.SetInputConnection( stlReader1.GetOutputPort())
stlActor1 = vtk. vtkActor( )
stlActor1. SetMapper (stlMapper1)
stlActor1.GetProperty().SetColor(196/255,202/255,212/255)  # Set color to gray
stlActor1.GetProperty().SetDiffuse(0.7)  # Set diffuse reflection to 90%
stlActor1.GetProperty().SetSpecular(0.6)  # Set specular reflection to 80%
stlActor1.GetProperty().SetSpecularPower(5)  # Set shininess to 40
renderer. AddActor (stlActor1)

stlReader1 = vtk. vtkSTLReader()
stlReader1.SetFileName( "3D models/DC1.stl" )
filter1 = vtk. vtkOutlineFilter()
filter1. SetInputConnection( stlReader1.GetOutputPort( ))
outLineMapper1 = vtk. vtkPolyDataMapper()
outLineMapper1.SetInputConnection(filter1. GetOutputPort( ))
stlMapper1 = vtk. vtkPolyDataMapper()
stlMapper1.SetInputConnection( stlReader1.GetOutputPort())
stlActor1 = vtk. vtkActor( )
stlActor1. SetMapper (stlMapper1)
stlActor1.GetProperty().SetColor(0/255,0/255,0/255)  # Set color to gray
stlActor1.GetProperty().SetDiffuse(0.7)  # Set diffuse reflection to 90%
stlActor1.GetProperty().SetSpecular(0.6)  # Set specular reflection to 80%
stlActor1.GetProperty().SetSpecularPower(5)  # Set shininess to 40
renderer. AddActor (stlActor1)

stlReader1 = vtk. vtkSTLReader()
stlReader1.SetFileName( "3D models/DC2.stl" )
filter1 = vtk. vtkOutlineFilter()
filter1. SetInputConnection( stlReader1.GetOutputPort( ))
outLineMapper1 = vtk. vtkPolyDataMapper()
outLineMapper1.SetInputConnection(filter1. GetOutputPort( ))
stlMapper1 = vtk. vtkPolyDataMapper()
stlMapper1.SetInputConnection( stlReader1.GetOutputPort())
stlActor1 = vtk. vtkActor( )
stlActor1. SetMapper (stlMapper1)
stlActor1.GetProperty().SetColor(0/255,0/255,0/255)  # Set color to gray
stlActor1.GetProperty().SetDiffuse(0.7)  # Set diffuse reflection to 90%
stlActor1.GetProperty().SetSpecular(0.6)  # Set specular reflection to 80%
stlActor1.GetProperty().SetSpecularPower(5)  # Set shininess to 40
renderer. AddActor (stlActor1)

stlReader1 = vtk. vtkSTLReader()
stlReader1.SetFileName( "3D models/DC3.stl" )
filter1 = vtk. vtkOutlineFilter()
filter1. SetInputConnection( stlReader1.GetOutputPort( ))
outLineMapper1 = vtk. vtkPolyDataMapper()
outLineMapper1.SetInputConnection(filter1. GetOutputPort( ))
stlMapper1 = vtk. vtkPolyDataMapper()
stlMapper1.SetInputConnection( stlReader1.GetOutputPort())
stlActor1 = vtk. vtkActor( )
stlActor1. SetMapper (stlMapper1)
stlActor1.GetProperty().SetColor(0/255,0/255,0/255)  # Set color to gray
stlActor1.GetProperty().SetDiffuse(0.7)  # Set diffuse reflection to 90%
stlActor1.GetProperty().SetSpecular(0.6)  # Set specular reflection to 80%
stlActor1.GetProperty().SetSpecularPower(5)  # Set shininess to 40
renderer. AddActor (stlActor1)

stlReader1 = vtk. vtkSTLReader()
stlReader1.SetFileName( "3D models/Propeller 1.stl" )
filter1 = vtk. vtkOutlineFilter()
filter1. SetInputConnection( stlReader1.GetOutputPort( ))
outLineMapper1 = vtk. vtkPolyDataMapper()
outLineMapper1.SetInputConnection(filter1. GetOutputPort( ))
stlMapper1 = vtk. vtkPolyDataMapper()
stlMapper1.SetInputConnection( stlReader1.GetOutputPort())
stlActor1 = vtk. vtkActor( )
stlActor1. SetMapper (stlMapper1)
stlActor1.GetProperty().SetColor(10/255,10/255,10/255)  # Set color to gray
stlActor1.GetProperty().SetDiffuse(0.7)  # Set diffuse reflection to 90%
stlActor1.GetProperty().SetSpecular(0.6)  # Set specular reflection to 80%
stlActor1.GetProperty().SetSpecularPower(5)  # Set shininess to 40
renderer. AddActor (stlActor1)

stlReader1 = vtk. vtkSTLReader()
stlReader1.SetFileName( "3D models/Propeller 2.stl" )
filter1 = vtk. vtkOutlineFilter()
filter1. SetInputConnection( stlReader1.GetOutputPort( ))
outLineMapper1 = vtk. vtkPolyDataMapper()
outLineMapper1.SetInputConnection(filter1. GetOutputPort( ))
stlMapper1 = vtk. vtkPolyDataMapper()
stlMapper1.SetInputConnection( stlReader1.GetOutputPort())
stlActor1 = vtk. vtkActor( )
stlActor1. SetMapper (stlMapper1)
stlActor1.GetProperty().SetColor(10/255,10/255,10/255)  # Set color to gray
stlActor1.GetProperty().SetDiffuse(0.7)  # Set diffuse reflection to 90%
stlActor1.GetProperty().SetSpecular(0.6)  # Set specular reflection to 80%
stlActor1.GetProperty().SetSpecularPower(5)  # Set shininess to 40
renderer. AddActor (stlActor1)

stlReader1 = vtk. vtkSTLReader()
stlReader1.SetFileName( "3D models/Propeller 3.stl" )
filter1 = vtk. vtkOutlineFilter()
filter1. SetInputConnection( stlReader1.GetOutputPort( ))
outLineMapper1 = vtk. vtkPolyDataMapper()
outLineMapper1.SetInputConnection(filter1. GetOutputPort( ))
stlMapper1 = vtk. vtkPolyDataMapper()
stlMapper1.SetInputConnection( stlReader1.GetOutputPort())
stlActor1 = vtk. vtkActor( )
stlActor1. SetMapper (stlMapper1)
stlActor1.GetProperty().SetColor(10/255,10/255,10/255)  # Set color to gray
stlActor1.GetProperty().SetDiffuse(0.7)  # Set diffuse reflection to 90%
stlActor1.GetProperty().SetSpecular(0.6)  # Set specular reflection to 80%
stlActor1.GetProperty().SetSpecularPower(5)  # Set shininess to 40
renderer. AddActor (stlActor1)

stlReader1 = vtk. vtkSTLReader()
stlReader1.SetFileName( "3D models/Propeller 4.stl" )
filter1 = vtk. vtkOutlineFilter()
filter1. SetInputConnection( stlReader1.GetOutputPort( ))
outLineMapper1 = vtk. vtkPolyDataMapper()
outLineMapper1.SetInputConnection(filter1. GetOutputPort( ))
stlMapper1 = vtk. vtkPolyDataMapper()
stlMapper1.SetInputConnection( stlReader1.GetOutputPort())
stlActor1 = vtk. vtkActor( )
stlActor1. SetMapper (stlMapper1)
stlActor1.GetProperty().SetColor(10/255,10/255,10/255)  # Set color to gray
stlActor1.GetProperty().SetDiffuse(0.7)  # Set diffuse reflection to 90%
stlActor1.GetProperty().SetSpecular(0.6)  # Set specular reflection to 80%
stlActor1.GetProperty().SetSpecularPower(5)  # Set shininess to 40
renderer. AddActor (stlActor1)

light1 = vtk.vtkLight()
light1.SetLightTypeToSceneLight()
light1.SetPosition(0.2, -2, 0.2)  # Set light position to the upper-left corner
renderer.AddLight(light1)
light2 = vtk.vtkLight()
light2.SetLightTypeToSceneLight()
light2.SetPosition(0, 1, 0.4)  # Set light position to the upper-left corner
renderer.AddLight(light2)
light3 = vtk.vtkLight()
light3.SetLightTypeToSceneLight()
light3.SetPosition(1, 1, 0.2)  # Set light position to the upper-left corner
renderer.AddLight(light3)

camera = renderer.GetActiveCamera()
camera.SetPosition(0, -0.65, 0.4)  # Set camera position to (0, 1, 0)
camera.SetFocalPoint(0, 0, 0.1)  # Set camera focal point to (0, 0, 0)
camera.SetViewUp(0, 0, 1)  # Set camera view up vector to (0, 0, -1)
interactor.Initialize()

window_to_image_filter = vtk.vtkWindowToImageFilter()
window_to_image_filter.SetInput(window)
window_to_image_filter.Update()

writer = vtk.vtkPNGWriter()
writer.SetFileName("Figures/eVTOL.png")
writer.SetInputData(window_to_image_filter.GetOutput())
writer.SetCompressionLevel(0)
writer.Write()

interactor.Start()