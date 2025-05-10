import streamlit as st
import numpy as np
from scipy import stats

# Title
st.title("Hypothesis Testing Tool")

class TTest:
    def __init__(self):
        self.sample = None
        self.sample1 = None
        self.sample2 = None

    def onesample(self):
        arrinput = st.text_input("Enter the sample array (Note: The array elements must be separated by whitespaces): ", key="onesample")
        self.sample = np.array(arrinput.split()).astype('int')
        teststats = st.radio('Test Statistics:', ['Population Variance', 'Population Mean'], key="onesample_radio")
        if teststats == 'Population Variance':
            option1 = st.radio('Options:', ['Population variance Known', 'Population variance Unknown'], key="onesample_option1")
            if option1 == 'Population variance Known':
                popvar = st.number_input('Enter the population variance:', key="onesample_popvar")
                t_stat, p_value = stats.ttest_1samp(self.sample, popvar)
                return t_stat, p_value
            elif option1 == 'Population variance Unknown':
                t_stat, p_value = stats.ttest_1samp(self.sample, 0)
                return t_stat, p_value
        elif teststats == 'Population Mean':
            option2 = st.radio('Options:', ['Population mean Known', 'Population mean Unknown'], key="onesample_option2")
            if option2 == 'Population mean Known':
                popmean = st.number_input('Enter the population mean:', key="onesample_popmean")
                t_stat, p_value = stats.ttest_1samp(self.sample, popmean)
                return t_stat, p_value
            elif option2 == 'Population mean Unknown':
                t_stat, p_value = stats.ttest_1samp(self.sample, 0)
                return t_stat, p_value

    def pairedttest(self):
        arrinput1 = st.text_input("Enter the sample array 1 (Note: The array elements must be separated by whitespaces): ", key="pairedttest1")
        self.sample1 = np.array(arrinput1.split()).astype('int')
        arrinput2 = st.text_input("Enter the sample array 2 (Note: The array elements must be separated by whitespaces): ", key="pairedttest2")
        self.sample2 = np.array(arrinput2.split()).astype('int')
        t_stat, p_value = stats.ttest_rel(self.sample1, self.sample2)
        return t_stat, p_value

    def twosample(self):
        arrinput1 = st.text_input("Enter the sample array 1 (Note: The array elements must be separated by whitespaces): ", key="twosample1")
        self.sample1 = np.array(arrinput1.split()).astype('int')
        arrinput2 = st.text_input("Enter the sample array 2 (Note: The array elements must be separated by whitespaces): ", key="twosample2")
        self.sample2 = np.array(arrinput2.split()).astype('int')
        option2 = st.radio('Options:', ['Equal Variance', 'Unequal Variance'], key="twosample_option2")
        if option2 == 'Equal Variance':
            t_stat, p_value = stats.ttest_ind(self.sample1, self.sample2, equal_var=True)
            return t_stat, p_value
        elif option2 == 'Unequal Variance':
            t_stat, p_value = stats.ttest_ind(self.sample1, self.sample2, equal_var=False)
            return t_stat, p_value

class ZTest:
    def __init__(self):
        self.sample1 = None
        self.sample2 = None

    def twosample(self):
        arrinput1 = st.text_input("Enter the sample array 1 (Note: The array elements must be separated by whitespaces): ", key="ztest_twosample1")
        self.sample1 = np.array(arrinput1.split()).astype('int')
        arrinput2 = st.text_input("Enter the sample array 2 (Note: The array elements must be separated by whitespaces): ", key="ztest_twosample2")
        self.sample2 = np.array(arrinput2.split()).astype('int')
        option1 = st.radio('Options:', ['Equal Variance, Known Population Variance', 'Equal Variance, Unknown Population Variance', 'Unequal Variance, Known Population Variance', 'Unequal Variance, Unknown Population Variance'], key="ztest_option1")
        if option1 == 'Equal Variance, Known Population Variance':
            pop_var1 = st.number_input("Enter the population variance for sample 1:", key="ztest_popvar1")
            pop_var2 = st.number_input("Enter the population variance for sample 2:", key="ztest_popvar2")
            t_stat, p_value = self.equal_var_known(pop_var1, pop_var2)
        elif option1 == 'Equal Variance, Unknown Population Variance':
            t_stat, p_value = self.equal_var_unknown()
        elif option1 == 'Unequal Variance, Known Population Variance':
            pop_var1 = st.number_input("Enter the population variance for sample 1:", key="ztest_popvar1")
            pop_var2 = st.number_input("Enter the population variance for sample 2:", key="ztest_popvar2")
            t_stat, p_value = self.unequal_var_known(pop_var1, pop_var2)
        elif option1 == 'Unequal Variance, Unknown Population Variance':
            t_stat, p_value = self.unequal_var_unknown()
        return t_stat, p_value

    def equal_var_known(self, pop_var1, pop_var2):
        n1 = len(self.sample1)
        n2 = len(self.sample2)
        mean1 = np.mean(self.sample1)
        mean2 = np.mean(self.sample2)

        if pop_var1 == 0 or pop_var2 == 0:
            st.warning("Population variance should not be zero.")
            return None, None

        pooled_std = np.sqrt((pop_var1 / n1) + (pop_var2 / n2))
        z_stat = (mean1 - mean2) / pooled_std
        p_value = 2 * stats.norm.cdf(-np.abs(z_stat))  # two-tailed test

        return z_stat, p_value

    def equal_var_unknown(self):
        t_stat, p_value = stats.ttest_ind(self.sample1, self.sample2, equal_var=True)
        return t_stat, p_value

    def unequal_var_known(self, pop_var1, pop_var2):
        n1 = len(self.sample1)
        n2 = len(self.sample2)
        mean1 = np.mean(self.sample1)
        mean2 = np.mean(self.sample2)

        se_diff = np.sqrt((pop_var1 / n1) + (pop_var2 / n2))
        z_stat = (mean1 - mean2) / se_diff
        p_value = 2 * stats.norm.cdf(-np.abs(z_stat))  # two-tailed test

        return z_stat, p_value

    def unequal_var_unknown(self):
        t_stat, p_value = stats.ttest_ind(self.sample1, self.sample2, equal_var=False)
        return t_stat, p_value

def main():
    option1 = st.radio('Select a test type', ['T test', 'Z test', 'Exit'], key="main_radio")
    if option1 == 'T test':
        t = TTest()
        option2 = st.radio('Select a T test', ['One sample test', 'Two Sample test', 'Paired Test'], key="t_test_radio")
        if option2 == 'One sample test':
            t_stat, p_value = t.onesample()
            if t_stat is not None and p_value is not None:
                st.write('The test statistics is', t_stat)
                st.write('The p_value is', p_value)
        elif option2 == 'Two Sample test':
            t_stat, p_value = t.twosample()
            if t_stat is not None and p_value is not None:
                st.write('The test statistics is', t_stat)
                st.write('The p_value is', p_value)
        elif option2 == 'Paired Test':
            t_stat, p_value = t.pairedttest()
            if t_stat is not None and p_value is not None:
                st.write('The test statistics is', t_stat)
                st.write('The p_value is', p_value)
    elif option1 == 'Z test':
        z = ZTest()
        t_stat, p_value = z.twosample()
        if t_stat is not None and p_value is not None:
            st.write('The test statistics is', t_stat)
            st.write('The p_value is', p_value)
    elif option1 == 'Exit':
        st.stop()

if __name__ == "__main__":
    main()
