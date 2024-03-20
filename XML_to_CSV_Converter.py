#Jay Anino
#jay.anino@nec.co.nz
#This program converts the test log for PQC into csv file.

import xml.etree.ElementTree as ET
import csv

# Get XML data
tree = ET.parse(r'')#provide file path to csv file
root = tree.getroot()

# Write to CSV
with open(r'', mode='w', newline='') as file: #provide save file path
    writer = csv.writer(file)

    # Headers
    writer.writerow([
        #ICOA
        'IMAGE_NAME', 'IMAGE_KEY', 'CURRENT_TIME', 'ELAPSED_TIME', 'STATUS',
        'ICAO_EXEC','ICAO_STAT','IMAGE_SIZE','IMAGE_SIZE_STATUS','WIDTH_TO_HEIGHT_RATIO','WIDTH_TO_HEIGHT_RATIO_STATUS', 
        'NUMBER_OF_FACES','NUMBER_OF_FACES_STATUS', 'EYE_DISTANCE', 'EYE_DISTANCE_STATUS',
        'EYE_WIDTH','EYE_WIDTH_STATUS', 'COLOUR_PROFILE','COLOUR_PROFILE_STATUS', 'HEAD_ROTATION_HOR','HEAD_ROTATION_HOR_STATUS', 
        'HEAD_POSITION_HOR','HEAD_POSITION_HOR_STATUS','HEAD_POSITION_VER','HEAD_POSITION_VER_STATUS',
        'HEAD_WIDTH','HEAD_WIDTH_STATUS', 'HEAD_LENGTH','HEAD_LENGTH_STATUS', 'BRIGHTNESS','BRIGHTNESS_STATUS', 
        'CONTRAST','CONTRAST_STATUS','COLOUR_CAST','COLOUR_CAST_STATUS', 'BLOCKY_ARTEFACTS','BLOCKY_ARTEFACTS_STATUS', 
        'SHARPNESS','SHARPNESS_STATUS', 'HEAD_ROTATION_VER','HEAD_ROTATION_VER_STATUS','RED_EYES','RED_EYES_STATUS',
        'FACESHADOW','FACESHADOW_STATUS', 'INTERFERING_BACKGROUND','INTERFERING_BACKGROUND_STATUS', 
        'GREY_VALUE_BACKGROUND','GREY_VALUE_BACKGROUND_STATUS','COLOUR_VARIATION_BACKGROUND', 'COLOUR_VARIATION_BACKGROUND_STATUS', 
        'GLASSES_SUNGLASSES','GLASSES_SUNGLASSES_STATUS', 'GLASSES_REFLECTION','GLASSES_REFLECTION_STATUS',
        'GLASSES_HEAVY_FRAME','GLASSES_HEAVY_FRAME_STATUS', 'EYE_CLOSED', 'EYE_CLOSED_STATUS','MOUTH_OPENED','MOUTH_OPENED_STATUS',
        #Detect Face
        'DETECT_FACE_EXEC','DETECT_FACE_STAT','HEAD_TOP_COOR','HEAD_LEFT_COOR','HEAD_RIGHT_COOR','HEAD_BOTTOM_COOR',
        'FACE_TOP_COOR','FACE_LEFT_COOR','FACE_RIGHT_COOR','FACE_BOTTOM_COOR',
        'RIGHT_EYE_VAL_1','RIGHT_EYE_VAL2','LEFT_EYE_VAL1','LEFT_EYE_VAL2',
        #Templating
        'TEMPLATING_EXEC','TEMPLATING_STAT','INDEX','FACE_CONFIDENCE','FACE_PAN','FACE_ROLL',
        'FACE_SCORE','FACE_TILT','FACIAL_POS_SCORE','FRONT_FACE_SCORE','HEAD_CONFIDENCE',
        'HEAD_SCORE',
        #Image Scale
        'IMAGE_SCALE_EXEC','IMAGE_SCALE_STAT','ORG_VAL_1','ORG_VAL_2','SCA_VAL_1','SCA_VAL_2','ORGSIZE','SCASIZE'
    ])

    # RESULT_INFO element
    for result_info in root.findall('.//RESULT_INFO'):
        image_name = result_info.find('IMAGE_NAME').text
        image_key = result_info.find('IMAGE_KEY').text
        current_time = result_info.find('CURRENT_TIME').text
        elapsed_time = result_info.find('ELAPSED_TIME').text
        status = result_info.find('STATUS').text

        # ICOA information
        icoa = result_info.find('ICOA')
        # ICOA EXEC
        icoa_exec = icoa.find('EXEC/VALUE1').text if icoa.find('EXEC/VALUE1') is not None else ''
        # ICOA STAT
        icoa_stat = icoa.find('STAT/VALUE1').text if icoa.find('STAT/VALUE1') is not None else ''
        # Image size
        image_size = icoa.find('IMAGE_SIZE/VALUE1').text if icoa.find('IMAGE_SIZE/VALUE1') is not None else ''
        image_size_status = icoa.find('IMAGE_SIZE/VALUE2').text if icoa.find('IMAGE_SIZE/VALUE2') is not None else ''
        # Width to height ratio
        width_to_height_ratio = icoa.find('WIDTH_TO_HEIGHT_RATIO/VALUE1').text if icoa.find('WIDTH_TO_HEIGHT_RATIO/VALUE1') is not None else ''
        width_to_height_ratio_status = icoa.find('WIDTH_TO_HEIGHT_RATIO/VALUE2').text if icoa.find('WIDTH_TO_HEIGHT_RATIO/VALUE2') is not None else ''
        # number of faces
        number_of_faces = icoa.find('NUMBER_OF_FACES/VALUE1').text if icoa.find('NUMBER_OF_FACES/VALUE1') is not None else ''
        number_of_faces_status = icoa.find('NUMBER_OF_FACES/VALUE2').text if icoa.find('NUMBER_OF_FACES/VALUE2') is not None else ''
        #Eye Distance
        eye_distance = icoa.find('EYE_DISTANCE/VALUE1').text if icoa.find('EYE_DISTANCE/VALUE1') is not None else ''
        eye_distance_status = icoa.find('EYE_DISTANCE/VALUE2').text if icoa.find('EYE_DISTANCE/VALUE2') is not None else ''
        #Eye Width
        eye_width = icoa.find('EYE_WIDTH/VALUE1').text if icoa.find('EYE_WIDTH/VALUE1') is not None else ''
        eye_width_status = icoa.find('EYE_WIDTH/VALUE2').text if icoa.find('EYE_WIDTH/VALUE2') is not None else ''
        #Colour Profile
        colour_profile = icoa.find('COLOUR_PROFILE/VALUE1').text if icoa.find('COLOUR_PROFILE/VALUE1') is not None else ''
        colour_profile_status = icoa.find('COLOUR_PROFILE/VALUE2').text if icoa.find('COLOUR_PROFILE/VALUE2') is not None else ''
        #Head Rotation Horizontal
        head_rotation_hor = icoa.find('HEAD_ROTATION_HOR/VALUE1').text if icoa.find('HEAD_ROTATION_HOR/VALUE1') is not None else ''
        head_rotation_hor_status = icoa.find('HEAD_ROTATION_HOR/VALUE2').text if icoa.find('HEAD_ROTATION_HOR/VALUE2') is not None else ''
        #Head Postion Horizontal
        head_position_hor = icoa.find('HEAD_POSITION_HOR/VALUE1').text if icoa.find('HEAD_POSITION_HOR/VALUE1') is not None else ''
        head_position_hor_status = icoa.find('HEAD_POSITION_HOR/VALUE2').text if icoa.find('HEAD_POSITION_HOR/VALUE2') is not None else ''
        #Head Position Vertical
        head_position_ver = icoa.find('HEAD_POSITION_VER/VALUE1').text if icoa.find('HEAD_POSITION_VER/VALUE1') is not None else ''
        head_position_ver_status= icoa.find('HEAD_POSITION_VER/VALUE2').text if icoa.find('HEAD_POSITION_VER/VALUE2') is not None else ''
        #Head Width
        head_width = icoa.find('HEAD_WIDTH/VALUE1').text if icoa.find('HEAD_WIDTH/VALUE1') is not None else ''
        head_width_status = icoa.find('HEAD_WIDTH/VALUE2').text if icoa.find('HEAD_WIDTH/VALUE2') is not None else ''
        #Head Length
        head_length = icoa.find('HEAD_LENGTH/VALUE1').text if icoa.find('HEAD_LENGTH/VALUE1') is not None else ''
        head_length_status = icoa.find('HEAD_LENGTH/VALUE2').text if icoa.find('HEAD_LENGTH/VALUE2') is not None else ''
        #Brigthness
        brightness = icoa.find('BRIGHTNESS/VALUE1').text if icoa.find('BRIGHTNESS/VALUE1') is not None else ''
        brightness_status = icoa.find('BRIGHTNESS/VALUE2').text if icoa.find('BRIGHTNESS/VALUE2') is not None else ''
        #Contrast
        contrast = icoa.find('CONTRAST/VALUE1').text if icoa.find('CONTRAST/VALUE1') is not None else ''
        contrast_status = icoa.find('CONTRAST/VALUE2').text if icoa.find('CONTRAST/VALUE2') is not None else ''
        #Colour Cast
        colour_cast = icoa.find('COLOUR_CAST/VALUE1').text if icoa.find('COLOUR_CAST/VALUE1') is not None else ''
        colour_cast_status = icoa.find('COLOUR_CAST/VALUE2').text if icoa.find('COLOUR_CAST/VALUE2') is not None else ''
        #Blocky Artefacts
        blocky_artefacts = icoa.find('BLOCKY_ARTEFACTS/VALUE1').text if icoa.find('BLOCKY_ARTEFACTS/VALUE1') is not None else ''
        blocky_artefacts_status = icoa.find('BLOCKY_ARTEFACTS/VALUE2').text if icoa.find('BLOCKY_ARTEFACTS/VALUE2') is not None else ''
        #Sharpness
        sharpness = icoa.find('SHARPNESS/VALUE1').text if icoa.find('SHARPNESS/VALUE1') is not None else ''
        sharpness_status = icoa.find('SHARPNESS/VALUE2').text if icoa.find('SHARPNESS/VALUE2') is not None else ''
        #Head Rotation Vertical
        head_rotation_ver = icoa.find('HEAD_ROTATION_VER/VALUE1').text if icoa.find('HEAD_ROTATION_VER/VALUE1') is not None else ''
        head_rotation_ver_status = icoa.find('HEAD_ROTATION_VER/VALUE2').text if icoa.find('HEAD_ROTATION_VER/VALUE2') is not None else ''
        #Red eyes
        red_eyes = icoa.find('RED_EYES/VALUE1').text if icoa.find('RED_EYES/VALUE1') is not None else ''
        red_eyes_status = icoa.find('RED_EYES/VALUE2').text if icoa.find('RED_EYES/VALUE2') is not None else ''
        #Face shadow
        faceshadow = icoa.find('FACESHADOW/VALUE1').text if icoa.find('FACESHADOW/VALUE1') is not None else ''
        faceshadow_status = icoa.find('FACESHADOW/VALUE2').text if icoa.find('FACESHADOW/VALUE2') is not None else ''
        #Interfering Background
        interfering_background = icoa.find('INTERFERING_BACKGROUND/VALUE1').text if icoa.find('INTERFERING_BACKGROUND/VALUE1') is not None else ''
        interfering_background_status = icoa.find('INTERFERING_BACKGROUND/VALUE2').text if icoa.find('INTERFERING_BACKGROUND/VALUE2') is not None else ''
        #Grey Value Background
        grey_value_background = icoa.find('GREY_VALUE_BACKGROUND/VALUE1').text if icoa.find('GREY_VALUE_BACKGROUND/VALUE1') is not None else ''
        grey_value_background_status = icoa.find('GREY_VALUE_BACKGROUND/VALUE2').text if icoa.find('GREY_VALUE_BACKGROUND/VALUE2') is not None else ''
        #Colour Variation Background
        colour_variation_background = icoa.find('COLOUR_VARIATION_BACKGROUND/VALUE1').text if icoa.find('COLOUR_VARIATION_BACKGROUND/VALUE1') is not None else ''
        colour_variation_background_status = icoa.find('COLOUR_VARIATION_BACKGROUND/VALUE2').text if icoa.find('COLOUR_VARIATION_BACKGROUND/VALUE2') is not None else ''
        #Glasses Sunglasses
        glasses_sunglasses = icoa.find('GLASSES_SUNGLASSES/VALUE1').text if icoa.find('GLASSES_SUNGLASSES/VALUE1') is not None else ''
        glasses_sunglasses_status = icoa.find('GLASSES_SUNGLASSES/VALUE2').text if icoa.find('GLASSES_SUNGLASSES/VALUE2') is not None else ''
        #Glasses Reflection
        glasses_reflection = icoa.find('GLASSES_REFLECTION/VALUE1').text if icoa.find('GLASSES_REFLECTION/VALUE1') is not None else ''
        glasses_reflection_status = icoa.find('GLASSES_REFLECTION/VALUE2').text if icoa.find('GLASSES_REFLECTION/VALUE2') is not None else ''
        #Glasses Heavy Frame
        glasses_heavy_frame = icoa.find('GLASSES_HEAVY_FRAME/VALUE1').text if icoa.find('GLASSES_HEAVY_FRAME/VALUE1') is not None else ''
        glasses_heavy_frame_status = icoa.find('GLASSES_HEAVY_FRAME/VALUE2').text if icoa.find('GLASSES_HEAVY_FRAME/VALUE2') is not None else ''
        #Eye Closed
        eye_closed = icoa.find('EYE_CLOSED/VALUE1').text if icoa.find('EYE_CLOSED/VALUE1') is not None else ''
        eye_closed_status = icoa.find('EYE_CLOSED/VALUE2').text if icoa.find('EYE_CLOSED/VALUE2') is not None else ''
        #Mouth Opened
        mouth_opened = icoa.find('MOUTH_OPENED/VALUE1').text if icoa.find('MOUTH_OPENED/VALUE1') is not None else ''
        mouth_opened_status = icoa.find('MOUTH_OPENED/VALUE2').text if icoa.find('MOUTH_OPENED/VALUE2') is not None else ''                

        #Detect Face Information
        detect_face = result_info.find('DETECT_FACE')
        # Detect Face EXEC
        detect_face_exec = detect_face.find('EXEC/VALUE1').text if detect_face.find('EXEC/VALUE1') is not None else ''
        # Detect Face STAT
        detect_face_stat = detect_face.find('STAT/VALUE1').text if detect_face.find('STAT/VALUE1') is not None else ''
        # Head Top Coordinate
        head_top_coor = detect_face.find('HEAD_TOP_COOR/VALUE1').text if detect_face.find('HEAD_TOP_COOR/VALUE1') is not None else ''
        # Head Left Coordinate
        head_left_coor= detect_face.find('HEAD_LEFT_COOR/VALUE1').text if detect_face.find('HEAD_LEFT_COOR/VALUE1') is not None else ''
        # Head Right Coordinate
        head_right_coor = detect_face.find('HEAD_RIGHT_COOR/VALUE1').text if detect_face.find('HEAD_RIGHT_COOR/VALUE1') is not None else ''
        # Head Bottom Coordinate
        head_bottom_coor = detect_face.find('HEAD_BOTTOM_COOR/VALUE1').text if detect_face.find('HEAD_BOTTOM_COOR/VALUE1') is not None else ''
        # Face Top Coordinate
        face_top_coor = detect_face.find('FACE_TOP_COOR/VALUE1').text if detect_face.find('FACE_TOP_COOR/VALUE1') is not None else ''
        # Face Left Coordinate
        face_left_coor = detect_face.find('FACE_LEFT_COOR/VALUE1').text if detect_face.find('FACE_LEFT_COOR/VALUE1') is not None else ''
        # Face Right Coordinate
        face_right_coor = detect_face.find('FACE_RIGHT_COOR/VALUE1').text if detect_face.find('FACE_RIGHT_COOR/VALUE1') is not None else ''
        # Face Bottom Coordinate
        face_bottom_coor = detect_face.find('FACE_BOTTOM_COOR/VALUE1').text if detect_face.find('FACE_BOTTOM_COOR/VALUE1') is not None else ''
        # Right Eye
        right_eye_val_1 = detect_face.find('RIGHT_EYE/VALUE1').text if detect_face.find('RIGHT_EYE/VALUE1') is not None else ''
        right_eye_val_2 = detect_face.find('RIGHT_EYE/VALUE2').text if detect_face.find('RIGHT_EYE/VALUE2') is not None else ''
        # Left Eye
        left_eye_val_1 = detect_face.find('LEFT_EYE/VALUE1').text if detect_face.find('LEFT_EYE/VALUE1') is not None else ''
        left_eye_val_2 = detect_face.find('LEFT_EYE/VALUE2').text if detect_face.find('LEFT_EYE/VALUE2') is not None else ''

        #Templating Information
        templating = result_info.find('TEMPLATING')
        # Templating EXEC
        templating_exec = templating.find('EXEC/VALUE1').text if templating.find('EXEC/VALUE1') is not None else ''
        # Templating STAT
        templating_stat = templating.find('STAT/VALUE1').text if templating.find('STAT/VALUE1') is not None else ''
        # Index
        index = templating.find('INDEX/VALUE1').text if templating.find('INDEX/VALUE1') is not None else ''
        # Face Confidence
        face_confidence = templating.find('FACE_CONFIDENCE/VALUE1').text if templating.find('FACE_CONFIDENCE/VALUE1') is not None else ''    
        # FACE PAN
        face_pan = templating.find('FACE_PAN/VALUE1').text if templating.find('FACE_PAN/VALUE1') is not None else ''
        # FACE ROLL
        face_roll = templating.find('FACE_ROLL/VALUE1').text if templating.find('FACE_ROLL/VALUE1') is not None else ''
        # FACE SCORE
        face_score = templating.find('FACE_SCORE/VALUE1').text if templating.find('FACE_SCORE/VALUE1') is not None else ''
        # Face Tilt
        face_tilt = templating.find('FACE_TILT/VALUE1').text if templating.find('FACE_TILT/VALUE1') is not None else ''
        # Facial Position Score
        facial_pos_score = templating.find('FACIAL_POS_SCORE/VALUE1').text if templating.find('FACIAL_POS_SCORE/VALUE1') is not None else ''
        # Front Face Score
        front_face_score = templating.find('FRONT_FACE_SCORE/VALUE1').text if templating.find('FRONT_FACE_SCORE/VALUE1') is not None else ''
        # Head Confidence
        head_confidence = templating.find('HEAD_CONFIDENCE/VALUE1').text if templating.find('HEAD_CONFIDENCE/VALUE1') is not None else ''
        # Head Score
        head_score = templating.find('HEAD_SCORE/VALUE1').text if templating.find('HEAD_SCORE/VALUE1') is not None else ''

        # Image Scale
        image_scale = result_info.find('IMAGE_SCALE')
        # Image Scale EXEC
        image_scale_exec = image_scale.find('EXEC/VALUE1').text if image_scale.find('EXEC/VALUE1') is not None else ''
        # Image Scale STAT
        image_scale_stat = image_scale.find('STAT/VALUE1').text if image_scale.find('STAT/VALUE1') is not None else ''
        # ORG Val 1
        org_val_1 = image_scale.find('ORG/VALUE1').text if image_scale.find('ORG/VALUE1') is not None else ''
        # ORG Val 2
        org_val_2 = image_scale.find('ORG/VALUE2').text if image_scale.find('ORG/VALUE2') is not None else ''
        # SCA Val 1
        sca_val_1 = image_scale.find('SCA/VALUE1').text if image_scale.find('SCA/VALUE1') is not None else ''
        # SCA Val 2
        sca_val_2 = image_scale.find('SCA/VALUE2').text if image_scale.find('SCA/VALUE2') is not None else ''
        # ORGSize
        orgsize = image_scale.find('ORGSIZE/VALUE1').text if image_scale.find('ORGSIZE/VALUE1') is not None else ''
        # SCASize
        scasize = image_scale.find('SCASIZE/VALUE1').text if image_scale.find('SCASIZE/VALUE1') is not None else ''

        # Write row to CSV
        writer.writerow([
            image_name, image_key, current_time, elapsed_time, status, 
            #ICAO
            icoa_exec,icoa_stat,image_size,image_size_status,
            width_to_height_ratio,width_to_height_ratio_status, 
            number_of_faces,number_of_faces_status, 
            eye_distance, eye_distance_status, 
            eye_width, eye_width_status,
            colour_profile, colour_profile_status,
            head_rotation_hor,head_rotation_hor_status, 
            head_position_hor,head_position_hor_status, 
            head_position_ver,head_position_ver_status,
            head_width,head_width_status,
            head_length,head_length_status, 
            brightness,brightness_status, 
            contrast,contrast_status, 
            colour_cast,colour_cast_status,
            blocky_artefacts,blocky_artefacts_status, 
            sharpness,sharpness_status, 
            head_rotation_ver,head_rotation_ver_status, 
            red_eyes,red_eyes_status, 
            faceshadow,faceshadow_status,
            interfering_background,interfering_background_status, 
            grey_value_background,grey_value_background_status, 
            colour_variation_background,colour_variation_background_status,
            glasses_sunglasses,glasses_sunglasses_status, 
            glasses_reflection,glasses_reflection_status, 
            glasses_heavy_frame,glasses_heavy_frame_status,
            eye_closed,eye_closed_status,mouth_opened,mouth_opened_status,
            #Detect Face
            detect_face_exec,detect_face_stat,head_top_coor,head_left_coor,
            head_right_coor, head_bottom_coor,face_top_coor,face_left_coor, 
            face_right_coor,face_bottom_coor, right_eye_val_1 ,right_eye_val_2, 
            left_eye_val_1,left_eye_val_2,
            #Templating
            templating_exec, templating_stat, index,
            face_confidence, face_pan, face_roll, face_score,
            face_tilt, facial_pos_score, front_face_score,
            head_confidence, head_score,
            #Image Scale
            image_scale_exec, image_scale_stat, org_val_1,
            org_val_2, sca_val_1, sca_val_2, orgsize, scasize
            ])
        
        print("File has been successfully converted to csv file.")