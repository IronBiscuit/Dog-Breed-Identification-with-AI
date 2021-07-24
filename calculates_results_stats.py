#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Yu Yang
# DATE CREATED: 19/07/2021                                 
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """ 
    
    #Extract relevant counts
    results_stats_dic = {}
    image_count = 0
    dog_image_count = 0
    notdog_image_count = 0
    correctly_classified_dog = 0
    correctly_classified_notdog = 0
    correctly_classified_dogbreed = 0
    labels_match_count = 0
    for key in results_dic:
        current_list = results_dic[key]
        pet_label = current_list[0]
        class_label = current_list[1]
        labels_match = current_list[2]
        pet_label_isdog = current_list[3]
        class_label_isdog = current_list[4]
        image_count += 1
        if (labels_match):
            labels_match_count += 1
        if (pet_label_isdog == 1):
            dog_image_count += 1
            if (class_label_isdog == 1):
                correctly_classified_dog += 1
            if (labels_match == 1):
                correctly_classified_dogbreed += 1
        else:
            notdog_image_count += 1
            if (class_label_isdog == 0):
                correctly_classified_notdog += 1
            
    correctly_classified_dog_percentage = (correctly_classified_dog / dog_image_count) * 100
    correctly_classified_notdog_percentage = (correctly_classified_notdog / notdog_image_count) * 100
    correctly_classified_dogbreed_percentage = (correctly_classified_dogbreed / dog_image_count) * 100
    
    #Set results_stats_dic values
    results_stats_dic["n_images"] = image_count
    results_stats_dic["n_dogs_img"] = dog_image_count
    results_stats_dic["n_notdogs_img"] = notdog_image_count
    results_stats_dic["n_labels_match"] = labels_match_count
    results_stats_dic["n_correctly_classified_dogs"] = correctly_classified_dog
    results_stats_dic["n_correctly_classified_notdogs"] = correctly_classified_notdog
    results_stats_dic["n_correctly_classified_breeds"] = correctly_classified_dogbreed
    results_stats_dic["pct_correct_dogs"] = correctly_classified_dog_percentage
    results_stats_dic["pct_correct_notdogs"] = correctly_classified_notdog_percentage
    results_stats_dic["pct_correct_breed"] = correctly_classified_dogbreed_percentage
        
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 
    return results_stats_dic
