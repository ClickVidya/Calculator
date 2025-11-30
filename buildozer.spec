[app]

# (str) Title of your application
title = CalculatorApp

# (str) Package name
package.name = calculatorapp

# (str) Package domain (reverse DNS style)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (str) The main .py file to use as the main entry point
source.main = app.py

# (list) List of inclusions using pattern matching
source.include_exts = py,png,kv

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# Kivy and pygame are needed
requirements = python3,kivy,pygame

# (str) Custom icon
# icon.filename = icon.png   # Uncomment if you have an icon

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) Supported orientation (portrait, landscape or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Presplash image
# presplash.filename = presplash.png

# (str) Icon for Android
# icon.filename = backspace.png  # Not recommended, use proper icon file

# (int) Target API
android.api = 33

# (int) Minimum API your app will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# Build Tools version
android.build_tools_version = 33.0.0


# (int) NDK version
android.ndk = 25b

# (bool) Indicate if the app should be packaged as debug
# debug = 1

# (str) Log level (debug, info, warning, error)
log_level = 2

# (list) Preserved Android Java classes for packaging
# android.add_src = 

# (list) Java .jar libraries to add
# android.add_jars = 

# (list) Permissions
# android.permissions = 

# (list) Android blacklist
# android.blacklist = 

# (list) Android whitelist
# android.whitelist = 

# (bool) Copy assets
# android.copy_assets = True

# (str) Application entry point for Android (Java/Kotlin)
# android.entrypoint = org.kivy.android.PythonActivity

# (list) Gradle dependencies
# android.gradle_dependencies =

# (str) Android logcat filters
# android.logcat_filters = *:S python:D

# (list) Android Java sources
# android.add_src = 

# (list) Android .so files to include
# android.add_libs_armeabi_v7a = 

# (list) Android .so files to include
# android.add_libs_arm64_v8a = 

# (list) Android extra Java libraries
# android.add_jars = 

# (list) Android extra AAR libraries
# android.add_aars = 

# (str) Android SDK license directory
# android.sdk_license = 

