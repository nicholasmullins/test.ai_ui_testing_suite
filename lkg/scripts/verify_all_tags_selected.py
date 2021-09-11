'''
This script allows you to control the threshold for a template match. Default is .65, the closer you set the falue to 1.0 the more it will act like a pixel match.
'''

import logging

log = logging.getLogger(__name__)

def run(context):
	found = context.wait_for_template_match(['all_tags_selected_tmp'], score_threshold=0.99, grayscale=False, canny=False, scale_invariant=False)
	assert found is not None, "All tags selected should be present"