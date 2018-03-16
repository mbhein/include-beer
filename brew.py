#!/usr/bin/env python3

""" Main script for brewing
    Usage:
        python3 brew.py

 Currently used only to control primary fermentation temperatures
 and record secondary/tertiary fermentation temperatures

"""
import configparser

def getProps(file):
    props = configparser.ConfigParser()
    props.read(file)
    return props

def main():
    #runtime objects
    mainPropsFile = './properties/main.properties'
    mainProps = getProps(mainPropsFile)
    print(mainProps['main'])
if __name__ == '__main__':
    main()
