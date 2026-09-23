from src.utils.logger import get_logger
import allure

logger = get_logger(__name__.split(".")[-1])

def verify(description: str, assertion_action: callable):
    logger.info(f"Verification: {description}")
    
    try:
        # The 'with' keyword creates the collapsible step in Allure
        with allure.step(f"Verify: {description}"):
            assertion_action() 
            logger.info(f"Verification passed ✅")
            
    except Exception as error:
        # Convert the massive error to a string
        error_msg = str(error)
        
        # Chop off the Aria snapshot if it exists!
        if "Call log:" in error_msg:
            # We split the string and keep only the clean part before the Call log
            clean_error_msg = error_msg.split("Call log:")[0].strip()
        elif "Aria snapshot:" in error_msg:
            clean_error_msg = error_msg.split("Aria snapshot:")[0].strip()
        else:
            clean_error_msg = error_msg

        logger.error(f"Verification failed ❌ - {clean_error_msg}")
        
        # Raise a new, clean exception for Pytest/Allure to catch
        raise AssertionError(clean_error_msg)